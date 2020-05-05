import json
import grpc
from google.protobuf.json_format import MessageToDict
from protobuf import slurm_pb2_grpc,slurm_pb2
from utils.read_conf import read_conf
from utils.CMD import CMD
import datetime
import getpass


_SPACE_='    '
_slurm_conf = read_conf()
_HOST = _slurm_conf['slurm_sim']['server']['host']
_PORT = _slurm_conf['slurm_sim']['server']['port']


def sacct():
    conn = grpc.insecure_channel("{}:{}".format(_HOST,_PORT))
    client = slurm_pb2_grpc.SlurmctldServiceStub(channel=conn)
    request = slurm_pb2.CMDRequest(cmd="sacct",type=CMD.SACCT.value)
    result = client.cmd(request).result
    print(result)

if __name__ == '__main__':
    sacct()
