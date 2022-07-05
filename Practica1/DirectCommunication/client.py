import xmlrpc.client
import sys

client_master = xmlrpc.client.ServerProxy('http://localhost:9000')

maxs=[]
mins=[]
i=1
while i<len(sys.argv):
    client_worker = xmlrpc.client.ServerProxy(client_master.listWorkers()[(i-1)%client_master.numWorkers()])
    print(client_worker.readCSV(sys.argv[i])+"\n")
    maxs.append(float(client_worker.max('Temp_max')))
    mins.append(float(client_worker.min('Temp_min')))
    i+=1

print("Temperatura maxima: "+str(max(maxs)))
print("Temperatura minima: "+str(min(mins)))