import xmlrpc.client
import sys

client_master = xmlrpc.client.ServerProxy('http://localhost:9000')

worker = client_master.getWorker(sys.argv[2])

client_worker = xmlrpc.client.ServerProxy(worker)

print(client_worker.readCSV(sys.argv[1]))