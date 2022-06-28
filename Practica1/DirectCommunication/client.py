import xmlrpc.client
import sys

client_master = xmlrpc.client.ServerProxy('http://localhost:9000')
worker = client_master.getWorker(sys.argv[2])

client_worker = xmlrpc.client.ServerProxy(worker)

#print(client_worker.readCSV(sys.argv[1]))
#print(client_worker.columns(sys.argv[1], 'Temp_max'))
#print(client_worker.groupby(sys.argv[1], 'Temp_max'))       # No se sap segur si funciona correctament.
#print(client_worker.head(sys.argv[1], 7))
#print(client_worker.isin(sys.argv[1], 'Temp_max', 25, 35))  # No funciona correctament.
#print(client_worker.items(sys.argv[1]))                     # No se sap segur si funciona correctament.
print(client_worker.max(sys.argv[1], 'Temp_max'))
#print(client_worker.min(sys.argv[1], 'Temp_min'))