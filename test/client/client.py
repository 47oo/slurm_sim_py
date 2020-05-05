import json

import grpc
from google.protobuf.json_format import MessageToDict

from test.protobuf import user_pb2, user_pb2_grpc

_HOST = 'localhost'
_PORT = '8080'

def run():

    # 连接到 grpc 服务器
    conn = grpc.insecure_channel(_HOST + ':' + _PORT)

    # 连接到相关的服务
    client = user_pb2_grpc.UserServiceStub(channel=conn)

    # 请求内容
    user    = client.GetUserById(user_pb2.DetailRequest(id=2))
    # 输出结果
    print('received:',json.dumps(MessageToDict(user)))

    # 请求内容
    users    = client.GetUsers(user_pb2.QueryUserListRequest(started_at=0,ended_at=0))
    # 输出结果
    print('received:',json.dumps(MessageToDict(users)))

if __name__ == '__main__':
    import datetime
    import time
    start_time = datetime.datetime.now()
    time.sleep(1)
    end_time = datetime.datetime.now()

    run_time = end_time + datetime.timedelta(seconds=1000*(end_time - start_time).seconds) - start_time
    print(run_time)