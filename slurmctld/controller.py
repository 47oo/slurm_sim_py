import logging

logging.basicConfig(level=logging.WARNING)
from concurrent import futures
from utils.CMD import CMD
import grpc
import time
import json
import datetime

from utils.read_conf import read_conf

from protobuf import slurm_pb2, slurm_pb2_grpc
from ClusterShell.NodeSet import NodeSet
from slurmctld import nodesfunc
from apscheduler.schedulers.background import BackgroundScheduler

_slurm_conf = read_conf()
_HOST = _slurm_conf['slurm_sim']['server']['host']
_PORT = _slurm_conf['slurm_sim']['server']['port']
_TIME_SPEED = _slurm_conf['slurm_sim']['timespeed']

# 初始化分区及节点
logging.info("init partition and nodes")
_partition_name = _slurm_conf['slurm_sim']['partition']['name']
_allnodes = _slurm_conf['slurm_sim']['partition']['nodelist']
_IDLE_NODES = NodeSet(_allnodes)
_ALLOC_NODES = NodeSet()
logging.info("finish partition: {} and nodelist: {}".format(_partition_name,_allnodes))

# 初始化作业列表
_R_JOBS = {}
_PD_JOBS = {}
_FH_JOBS = {}

'''
    实现grbc自定义方法
'''


class SlurmCtldService(slurm_pb2_grpc.SlurmctldServiceServicer):

    def cmd(self, request, context):
        cmd = request.cmd
        cmd_type = request.type
        if cmd_type == CMD.SINFO.value:
            result = nodesfunc.sinfo(_partition_name,_IDLE_NODES,_ALLOC_NODES)
        elif cmd_type == CMD.SRUN.value:
            jobid = nodesfunc.get_jobid()
            cmd = json.loads(cmd)
            submit_time = datetime.datetime.now()
            cmd['submit_time'] = submit_time
            result = nodesfunc.srun(cmd,_IDLE_NODES,_ALLOC_NODES,jobid,_R_JOBS,_PD_JOBS,_FH_JOBS)
        elif cmd_type == CMD.SQUEUE.value:
            result = nodesfunc.squeue(_R_JOBS,_PD_JOBS)
        else:
            result = "Unsupport This Cmd"
        response = slurm_pb2.ResultResponse(result = result)
        return response


def sim_controller():
    logging.info("start slurmctld")
    sim_server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    slurm_pb2_grpc.add_SlurmctldServiceServicer_to_server(SlurmCtldService(), sim_server)
    sim_server.add_insecure_port("{}:{}".format(_HOST, _PORT))
    logging.info("sim start with {}:{}".format(_HOST, _PORT))
    sim_server.start()
    logging.info("init BlockingScheduler")
    # 等待结束，不然进程会立刻退出
    pd_check_scheduler = BackgroundScheduler()
    pd_check_scheduler.add_job(nodesfunc.pd_check_to_run,'interval',
                               (_IDLE_NODES,_ALLOC_NODES,_R_JOBS,_PD_JOBS,_FH_JOBS),seconds=1)
    pd_check_scheduler.start()
    logging.info("scheduler start")
    nodesfunc.run_end_scheduler.start()
    print("sim start with {}:{}".format(_HOST, _PORT))

    try:
        nodesfunc.pd_check_to_run(_IDLE_NODES,_ALLOC_NODES,_R_JOBS,_PD_JOBS,_FH_JOBS)
        while True:
            time.sleep(60 * 60 * 24)
    except KeyboardInterrupt:
        # pd_check_scheduler.remove_all_jobs()
        pd_check_scheduler.shutdown()
        nodesfunc.run_end_scheduler.shutdown()
        sim_server.stop(0)

    logging.info("scheduler stop ")
    logging.info("sim stop")


if __name__ == '__main__':
    sim_controller()
