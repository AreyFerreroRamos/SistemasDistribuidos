import grpc
from concurrent import futures
import time

import insultingServer_pb2
import insultingServer_pb2_grpc

from InsultingService import insultingService

class InsultingServiceServicer(insultingServer_pb2_grpc.InsultingServiceServicer):
    def AddInsult(self, request, context):
        response = insultingServer_pb2.Insult()
        response.value = insultingService.add_insult(request.value)
        return response
    
    def GetInsults(self, request, context):
        response = insultingServer_pb2.Insults()
        response.value.extend(insultingService.get_insults())
        return response

    def Insultme(self, request, context):
        response = insultingServer_pb2.Insult()
        response.value = insultingService.insultme()
        return response

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

insultingServer_pb2_grpc.add_InsultingServiceServicer_to_server(InsultingServiceServicer(), server)

print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)