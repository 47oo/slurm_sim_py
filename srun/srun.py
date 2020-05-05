import os
import getpass
import sys,getopt
import json
import grpc
from protobuf import slurm_pb2_grpc,slurm_pb2
from utils.read_conf import read_conf
from utils.CMD import CMD



_SPACE_='    '
_slurm_conf = read_conf()
_HOST = _slurm_conf['slurm_sim']['server']['host']
_PORT = _slurm_conf['slurm_sim']['server']['port']


def srun(cmd):
    conn = grpc.insecure_channel("{}:{}".format(_HOST,_PORT))
    client = slurm_pb2_grpc.SlurmctldServiceStub(channel=conn)
    request = slurm_pb2.CMDRequest(cmd=cmd,type=CMD.SRUN.value)
    result = client.cmd(request).result
    print(result)

if __name__ == '__main__':
    cmd = json.dumps({
        'nodelist': 'cn[1]',
        'real_runtime': 20,
        'username': getpass.getuser()
    })
    srun(cmd)

