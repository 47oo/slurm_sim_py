import logging
from concurrent import futures


import grpc
import time

from test.protobuf import user_pb2, user_pb2_grpc

_HOST = 'localhost'
_PORT = '8080'

class UserService(user_pb2_grpc.UserServiceServicer):
    def GetUserById(self,request,context):
        user_id = request.id
        return user_pb2.User(id=request.id,
            username="yufei" + str(request.id))

    def GetUsers(self,request,context):
        users = user_pb2.UserList()
        users.users.append(user_pb2.User(id=1,username="yufei1"))
        users.users.append(user_pb2.User(id=2,username="yufei2"))
        return users;

def serve():

    # 指定最多可以有 4 个线程来处理请求
    grpcServer = grpc.server(futures.ThreadPoolExecutor(max_workers=4))

    # 将相应的服务注册到 grpc 中
    user_pb2_grpc.add_UserServiceServicer_to_server(UserService(), grpcServer)

    # 指定端口并且非 ssl 模式
    grpcServer.add_insecure_port(_HOST + ':' + _PORT)
    grpcServer.start()

    # 等待结束，不然进程会立刻退出
    try:
        while True:
            time.sleep(60 * 60 * 24)
    except KeyboardInterrupt:
        grpcServer.stop(0)


if __name__ == '__main__':
    logging.basicConfig()
    serve()
