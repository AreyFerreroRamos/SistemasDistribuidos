import grpc

import insultingServer_pb2
import insultingServer_pb2_grpc

channel = grpc.insecure_channel('localhost:50051')

stub = insultingServer_pb2_grpc.InsultingServiceStub(channel)

new_insult = insultingServer_pb2.Insult(value='payaso')
stub.AddInsult(new_insult)

new_insult = insultingServer_pb2.Insult(value='impresentable')
stub.AddInsult(new_insult)

new_insult = insultingServer_pb2.Insult(value='ignorante')
stub.AddInsult(new_insult)

new_insult = insultingServer_pb2.Insult(value='perdedor')
stub.AddInsult(new_insult)

print(stub.GetInsults(new_insult))

print(stub.Insultme(new_insult))