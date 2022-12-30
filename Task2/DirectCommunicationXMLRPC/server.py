from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client
import threading
import logging
import time
import sys
import os
import nodeType
import serverFunctions

def ping_nodes(node):
    if (node.getNodeType() == "master"):
        proxy_master = xmlrpc.client.ServerProxy('http://localhost:'+sys.argv[1], allow_none=True)
    else:
        proxy_worker = xmlrpc.client.ServerProxy('http://localhost:'+sys.argv[2], allow_none=True)
        workers=[]

    while True:
        if event.is_set():
            break
        else:
            if (node.getNodeType() == "master"):
                for worker in proxy_master.listWorkers():
                    try:
                        xmlrpc.client.ServerProxy(worker, allow_none=True).isAlive()
                    except:
                        proxy_master.removeWorker(worker.split(':')[2])
            else:
                try:
                    proxy_master = xmlrpc.client.ServerProxy(proxy_worker.getMaster(), allow_none=True)
                    proxy_master.isAlive()
                    workers = proxy_master.listWorkers()
                except:
                    for worker in workers:
                        proxy = xmlrpc.client.ServerProxy(worker, allow_none=True)
                        isLeader = proxy.canBeLeader(worker.split(':')[2], sys.argv[2])
                        if (isLeader == False):
                            break
                    if (isLeader == True):
                        node.setNodeType("master")
                        workers.remove('http://localhost:'+sys.argv[2])
                        proxy_master = xmlrpc.client.ServerProxy('http://localhost:'+sys.argv[2], allow_none=True)
                        for worker in workers:
                            proxy_master.addWorker(worker)
                            proxy_worker = xmlrpc.client.ServerProxy(worker, allow_none=False)
                            proxy_worker.setMaster('http://localhost:'+sys.argv[2])
        time.sleep(1)

node = nodeType.NodeType()
logging.basicConfig(level=logging.INFO)

if (len(sys.argv) == 2):
    node.setNodeType("master")

    server = SimpleXMLRPCServer(('localhost', int(sys.argv[1])), logRequests=True, allow_none=True)
else:
    node.setNodeType("worker")

    proxy = xmlrpc.client.ServerProxy('http://localhost:'+sys.argv[1], allow_none=True)
    proxy.addWorker('http://localhost:'+sys.argv[2])
    
    server = SimpleXMLRPCServer(('localhost', int(sys.argv[2])), logRequests=True, allow_none=True)

server.register_instance(serverFunctions.ServerFunctions('http://localhost:'+sys.argv[1]))

name_thread = threading.Thread(target=ping_nodes, args=(node,))

try:
    print('Use control + c to exit the '+node.getNodeType()+' node.')
    event = threading.Event()
    name_thread.start()
    server.serve_forever()
except KeyboardInterrupt:
    print('Exiting '+node.getNodeType()+' node...')
    event.set()
    name_thread.join()