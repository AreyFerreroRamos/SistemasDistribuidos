import xmlrpc.client
import sys

import grpc
import daskFunctions_pb2
import daskFunctions_pb2_grpc

client_master = xmlrpc.client.ServerProxy('http://localhost:9000')

#maxs=[]
#mins=[]
i=1

while i<len(sys.argv):
    channel = grpc.insecure_channel('localhost:'+client_master.listWorkers()[(i-1)%client_master.numWorkers()].split(':')[2])
    client_worker = daskFunctions_pb2_grpc.DaskFunctionsStub(channel)
    name_file = daskFunctions_pb2.NameFile(value=sys.argv[i])
    print(client_worker.ReadCSV(name_file).value+"\n")
    #maxs.append(float(client_worker.Max(field).value))
    #mins.append(float(client_worker.min('Temp_min')))
    i+=1

#print("Temperatura maxima: "+str(max(maxs)))
#print("Temperatura minima: "+str(min(mins)))