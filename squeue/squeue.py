import json
import grpc
from google.protobuf.json_format import MessageToDict
from protobuf import slurm_pb2_grpc,slurm_pb2
from utils.read_conf import read_conf
from utils.CMD import CMD
import datetime


_SPACE_='    '
_slurm_conf = read_conf()
_HOST = _slurm_conf['slurm_sim']['server']['host']
_PORT = _slurm_conf['slurm_sim']['server']['port']


def squeue():
    conn = grpc.insecure_channel("{}:{}".format(_HOST,_PORT))
    client = slurm_pb2_grpc.SlurmctldServiceStub(channel=conn)

    request = slurm_pb2.CMDRequest(cmd="squeue",type=CMD.SQUEUE.value)
    result = json.loads(client.cmd(request).result)
    print("{0:10}{1:10}{2:10}{3:10}{4:15}".format("JobId","Username","State","Runtime","NodeList"))
    for jobid in result:
        print("{0:10}{1:10}{2:10}{3:10}{4:15}".format(jobid,result[jobid]['username'],result[jobid]['state'],
                                            result[jobid]['runtime'].split('.')[0],
                                            result[jobid]['nodelist']))


if __name__ == '__main__':
    squeue()
