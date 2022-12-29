from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client
import threading
import logging
import time
import sys
import os
import managerFunctions
import serverFunctions

def ping_nodes(manager):
    if (manager.getNodeType() == "master"):
        client_master = xmlrpc.client.ServerProxy('http://localhost:'+sys.argv[1], allow_none=True)
    else:
        client_worker = xmlrpc.client.ServerProxy('http://localhost:'+sys.argv[2], allow_none=True)

    while True:
        if event.is_set():
            break
        else:
            if (manager.getNodeType() == "master"):
                for worker in client_master.listWorkers():
                    try:
                        xmlrpc.client.ServerProxy(worker, allow_none=True).isAlive()
                    except:
                        client_master.removeWorker(worker.split(':')[2])
            else:
                try:
                    xmlrpc.client.ServerProxy(client_worker.getMaster()).isAlive()
                except:
                    for worker in client_worker.listWorkers():
                        client_candidate = xmlrpc.client.ServerProxy(worker, allow_none=True)
                        isLeader = client_candidate.canBeLeader(worker.split(':')[2], sys.argv[2])
                        if (isLeader == False):
                            break
                    if (isLeader == True):
                        manager.setNodeType("master")
                        client_master = xmlrpc.client.ServerProxy('http://localhost:'+sys.argv[2], allow_none=True)
                        client_master.removeWorker(sys.argv[2])
                        for worker in client_master.listWorkers():
                            client_worker = xmlrpc.client.ServerProxy(worker, allow_none=False)
                            client_worker.setMaster('http://localhost:'+sys.argv[2])
        time.sleep(1)

manager = managerFunctions.ManagerFunctions()
logging.basicConfig(level=logging.INFO)

if (len(sys.argv) == 2):
    manager.setNodeType("master")

    server = SimpleXMLRPCServer(('localhost', int(sys.argv[1])), logRequests=True, allow_none=True)
else:
    manager.setNodeType("worker")

    proxy_master = xmlrpc.client.ServerProxy('http://localhost:'+sys.argv[1], allow_none=True)
    proxy_master.addWorker('http://localhost:'+sys.argv[2])

    server = SimpleXMLRPCServer(('localhost', int(sys.argv[2])), logRequests=True, allow_none=True)

server.register_instance(serverFunctions.ServerFunctions('http://localhost:'+sys.argv[1]))

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