import grpc

import functions_pb2
import functions_pb2_grpc

channel = grpc.insecure_channel('localhost:50051')

stub = functions_pb2_grpc.FunctionsStub(channel)

new_insult = functions_pb2.Insult(value='Desastre')
print(new_insult)

stub.AddInsult(new_insult)
print(stub.GetInsults(new_insult))
print(stub.Insultme(new_insult))