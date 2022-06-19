import grpc
from concurrent import futures
import time

import functions_pb2
import functions_pb2_grpc

import functions

class FunctionsServicer(functions_pb2_grpc.FunctionsServicer):
    def AddInsult(self, request, context):
        response = functions_pb2.Insult()
        response.insult = functions.add_insult(request.insult)
        return response
    
    def GetInsults(self, request, context):
        response = functions.get_insults()
        return response

    def Insultme(self, request, context):
        response = functions.insultme()
        return response

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

functions_pb2_grpc.add_FunctionsServicer_to_server(FunctionsServicer(), server)

print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)