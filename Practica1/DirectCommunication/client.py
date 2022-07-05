import xmlrpc.client
import pandas
import sys

client_master = xmlrpc.client.ServerProxy('http://localhost:9000')
#client_worker = xmlrpc.client.ServerProxy(client_master.listWorkers()[0])

abs_max=0.0
abs_min=100.0
i=1
while i<len(sys.argv):
    client_worker = xmlrpc.client.ServerProxy(client_master.listWorkers()[(i-1)%client_master.numWorkers()])
    client_worker.readCSV(sys.argv[i])
    local_max=float(client_worker.max('Temp_max'))
    if (abs_max<local_max):
        abs_max=local_max
    local_min=float(client_worker.min('Temp_min'))
    if (abs_min>local_min):
        abs_min=local_min
    i+=1

print("Temperatura maxima: "+str(abs_max))
print("Temperatura minima: "+str(abs_min))