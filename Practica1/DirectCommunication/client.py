import xmlrpc.client
import sys

client_master = xmlrpc.client.ServerProxy('http://localhost:9000')

abs_max=0.0
abs_min=100.0
i=1
while i<len(sys.argv):
    client_worker = xmlrpc.client.ServerProxy(client_master.listWorkers()[(i-1)%client_master.numWorkers()])
    local_max=float(client_worker.max(sys.argv[i], 'Temp_max'))
    if (abs_max<local_max):
        abs_max=local_max
    local_min=float(client_worker.min(sys.argv[i], 'Temp_min'))
    if (abs_min>local_min):
        abs_min=local_min
    i+=1

print("Temperatura maxima: "+str(abs_max))
print("Temperatura minima: "+str(abs_min))

#print(client_worker.readCSV(sys.argv[i]))
#print(client_worker.columns(sys.argv[1], 'Temp_max'))
#print(client_worker.groupby(sys.argv[1], 'Temp_max'))       # No se sap segur si funciona correctament.
#print(client_worker.head(sys.argv[1], 7))
#print(client_worker.isin(sys.argv[1], 'Temp_max', 25, 35))  # No funciona correctament.
#print(client_worker.items(sys.argv[1]))                     # No se sap segur si funciona correctament.