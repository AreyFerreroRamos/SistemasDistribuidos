import grpc

import functions_pb2
import functions_pb2_grpc

channel = grpc.insecure_channel('localhost:50051')

stub = functions_pb2_grpc.FunctionsStub(channel)

new_insult = functions_pb2.Insult(insult='')

response = stub.Insultme(new_insult)
print(response.insult)