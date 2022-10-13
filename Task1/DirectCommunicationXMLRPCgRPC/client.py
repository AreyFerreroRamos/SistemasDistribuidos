import xmlrpc.client
import threading
import sys

import grpc
import daskFunctions_pb2
import daskFunctions_pb2_grpc

def treat_file(client_worker, i, maxs, mins):
    name_file = daskFunctions_pb2.NameFile(name_file=sys.argv[i])
    print(client_worker.ReadCSV(name_file).value+"\n")
    field = daskFunctions_pb2.Field(field='Temp_max')
    maxs.append(float(client_worker.Max(field).value))
    field = daskFunctions_pb2.Field(field='Temp_min')
    mins.append(float(client_worker.Min(field).value))

client_master = xmlrpc.client.ServerProxy('http://localhost:9000')

threads=[]
maxs=[]
mins=[]

i=1
while i<len(sys.argv):
    num_worker=0
    while ((num_worker<client_master.numWorkers()) and (i<len(sys.argv))):
        channel = grpc.insecure_channel('localhost:'+client_master.listWorkers()[num_worker].split(':')[2])
        client_worker = daskFunctions_pb2_grpc.DaskFunctionsStub(channel)
        threads.append(threading.Thread(target=treat_file, name="thread%s" %i, args=(client_worker, i, maxs, mins)))
        threads[num_worker].start()
        num_worker+=1
        i+=1
    num_worker=0
    while (num_worker<len(threads)):
        threads[num_worker].join()
        num_worker+=1
    threads.clear()

print("Temperatura maxima: "+str(round(max(maxs), 2)))
print("Temperatura minima: "+str(round(min(mins), 2)))