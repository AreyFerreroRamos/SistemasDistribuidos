import xmlrpc.client
import sys
import os

import grpc
from concurrent import futures
import time

import daskFunctions_pb2
import daskFunctions_pb2_grpc

import daskFunctions

proxy = xmlrpc.client.ServerProxy('http://localhost:9000')
proxy.addWorker('http://localhost:'+sys.argv[1])

class DaskFunctionsServicer(daskFunctions_pb2_grpc.DaskFunctionsServicer):
    def ReadCSV(self, request, context):
        response = daskFunctions_pb2.FileReturn()
        response.value = daskFunctions.DaskFunctions().readCSV(request.name_file)
        return response

    def Max(self, request, context):
        response = daskFunctions_pb2.ValueReturn()
        response.value = daskFunctions.DaskFunctions().max(request.name_file, request.field)
        return response

    def Min(self, request, context):
        response = daskFunctions_pb2.ValueReturn()
        response.value = daskFunctions.DaskFunctions().min(request.name_file, request.field)
        return response

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

daskFunctions_pb2_grpc.add_DaskFunctionsServicer_to_server(DaskFunctionsServicer(), server)

print('Starting server. Listening on port '+sys.argv[1]+'.')
server.add_insecure_port('[::]:'+sys.argv[1])
server.start()

try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
    proxy.removeWorker(sys.argv[1])