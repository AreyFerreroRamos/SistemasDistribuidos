from xmlrpc.server import SimpleXMLRPCServer
import logging
import os

master = SimpleXMLRPCServer(('localhost', 9000), logRequests=True)
logging.basicConfig(level=logging.INFO)

workers=[]

def addWorker(worker):
    workers.append(worker)
    return ' '

def listWorkers():
    return list(workers)

def removeWorker(port):
    for worker in workers:
        if port==worker.split(':')[2]:
            workers.remove(worker)
    return ' '

master.register_function(addWorker)
master.register_function(listWorkers)
master.register_function(removeWorker)

try:
    print('Use control + c to exit the Master node')
    master.serve_forever()
except KeyboardInterrupt:
    print('Exiting master node')