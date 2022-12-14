from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client
import threading
import logging
import time
import sys
import os
import serverFunctions

def treat_ping_master(server):
    while True:
        # Pings.
        if event.is_set():
            break
        else:
            time.sleep(1)

def treat_ping_worker(server):
    while True:
        if event.is_set():
            break
        else:
            master = server.getMaster()
            response = os.system("ping -c 1 "+master)
            if (response != 0):
                server.addMaster(server.getWorker())
            else:
                server.addMaster(master)
            time.sleep(1)

logging.basicConfig(level=logging.INFO)

if (len(sys.argv) == 1):
    node="master"
    server = SimpleXMLRPCServer(('localhost', 9000), logRequests=True)

    name_thread = threading.Thread(target=treat_ping_master)
else:
    node="worker"
    proxy = xmlrpc.client.ServerProxy('http://localhost:9000')
    proxy.addWorker('http://localhost:'+sys.argv[1])

    server = SimpleXMLRPCServer(('localhost', int(sys.argv[1])), logRequests=True)

    name_thread = threading.Thread(target=treat_ping_worker, args=(server))

server.register_instance(serverFunctions.ServerFunctions())

try:
    print('Use control + c to exit the '+node+' node.')
    event = threading.Event()
    name_thread.start()
    server.serve_forever()
except KeyboardInterrupt:
    print('Exiting '+node+' node...')
    event.set()
    name_thread.join()
    if (len(sys.argv) == 2):
        proxy.removeWorker(sys.argv[1])