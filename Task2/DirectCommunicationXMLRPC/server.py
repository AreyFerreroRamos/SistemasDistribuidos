from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client
import threading
import logging
import time
import sys
import os
import masterManagerFunctions
import workerFunctions

def ping_nodes(node, master_manager):
    mutex = threading.Lock()
    if (node == "master"):
        client_master = xmlrpc.client.ServerProxy(master_manager.getMaster())
    
    while True:
        if event.is_set():
            break
        else:
            if (node == "master"):
                for worker in client_master.listWorkers():
                    try:
                        xmlrpc.client.ServerProxy(worker).isAlive()
                    except:
                        client_master.removeWorker(worker.split(':')[2])
            else:
                mutex.acquire()
                try:
                    xmlrpc.client.ServerProxy(master_manager.getMaster()).isAlive()
                except:
                    node="master"
                    master_manager.setMaster('http://localhost:'+sys.argv[1])
                    client_master = xmlrpc.client.ServerProxy('http://localhost:'+sys.argv[1])
                    client_master.removeWorker(sys.argv[1])
                mutex.release()
        time.sleep(1)

master_manager = masterManagerFunctions.MasterManagerFunctions()
logging.basicConfig(level=logging.INFO)

if (len(sys.argv) == 1):
    node="master"
    
    master_manager.setMaster('http://localhost:9000')
    server = SimpleXMLRPCServer(('localhost', 9000), logRequests=True)
else:
    node="worker"
    
    proxy = xmlrpc.client.ServerProxy(master_manager.getMaster())
    proxy.addWorker('http://localhost:'+sys.argv[1])

    server = SimpleXMLRPCServer(('localhost', int(sys.argv[1])), logRequests=True)

server.register_instance(workerFunctions.WorkerFunctions())
name_thread = threading.Thread(target=ping_nodes, args=(node, master_manager))

try:
    print('Use control + c to exit the '+node+' node.')
    event = threading.Event()
    name_thread.start()
    server.serve_forever()
except KeyboardInterrupt:
    print('Exiting node...')
    event.set()
    name_thread.join()