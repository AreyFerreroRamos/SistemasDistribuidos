from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client
import threading
import logging
import time
import sys
import os
import managerFunctions
import workerFunctions

def ping_nodes(manager):
    if (manager.getNodeType() == "master"):
        client_master = xmlrpc.client.ServerProxy(manager.getMaster())
    else:
        mutex = threading.Lock()

    while True:
        if event.is_set():
            break
        else:
            if (manager.getNodeType() == "master"):
                for worker in client_master.listWorkers():
                    try:
                        xmlrpc.client.ServerProxy(worker).isAlive()
                    except:
                        client_master.removeWorker(worker.split(':')[2])
            else:
                mutex.acquire()
                try:
                    xmlrpc.client.ServerProxy(manager.getMaster()).isAlive()
                except:
                    manager.setNodeType("master")
                    manager.setMaster('http://localhost:'+sys.argv[1])
                    client_master = xmlrpc.client.ServerProxy('http://localhost:'+sys.argv[1])
                    client_master.removeWorker(sys.argv[1])
                mutex.release()
        time.sleep(1)

manager = managerFunctions.ManagerFunctions()
logging.basicConfig(level=logging.INFO)

if (len(sys.argv) == 1):
    manager.setNodeType("master")
    manager.setMaster('http://localhost:9000')
    
    server = SimpleXMLRPCServer(('localhost', 9000), logRequests=True)
else:
    manager.setNodeType("worker")
    
    proxy = xmlrpc.client.ServerProxy(manager.getMaster())
    proxy.addWorker('http://localhost:'+sys.argv[1])

    server = SimpleXMLRPCServer(('localhost', int(sys.argv[1])), logRequests=True)

server.register_instance(workerFunctions.WorkerFunctions())
name_thread = threading.Thread(target=ping_nodes, args=(manager,))

try:
    print('Use control + c to exit the '+manager.getNodeType()+' node.')
    event = threading.Event()
    name_thread.start()
    server.serve_forever()
except KeyboardInterrupt:
    print('Exiting '+manager.getNodeType()+' node...')
    event.set()
    name_thread.join()