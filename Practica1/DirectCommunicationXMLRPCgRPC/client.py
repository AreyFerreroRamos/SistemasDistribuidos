import xmlrpc.client
import sys

import grpc
import daskFunctions_pb2
import daskFunctions_pb2_grpc

client_master = xmlrpc.client.ServerProxy('http://localhost:9000')

maxs=[]
mins=[]
i=1

while i<len(sys.argv):
    channel = grpc.insecure_channel('localhost:'+client_master.listWorkers()[(i-1)%client_master.numWorkers()].split(':')[2])
    client_worker = daskFunctions_pb2_grpc.DaskFunctionsStub(channel)
    name_file = daskFunctions_pb2.NameFile(name_file=sys.argv[i])
    print(client_worker.ReadCSV(name_file).value+"\n")
    max_atributes = daskFunctions_pb2.Field(name_file=sys.argv[i], field='Temp_max')
    maxs.append(float(client_worker.Max(max_atributes).value))
    min_attributes = daskFunctions_pb2.Field(name_file=sys.argv[i], field='Temp_min')
    mins.append(float(client_worker.Min(min_attributes).value))
    i+=1

print("Temperatura maxima: "+str(max(maxs)))
print("Temperatura minima: "+str(min(mins)))