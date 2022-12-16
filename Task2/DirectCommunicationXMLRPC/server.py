from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client
import threading
import logging
import time
import sys
import os
import masterManagerFunctions
import workerFunctions

#def treat_ping_master(server):
 #   while True:
  #      if event.is_set():
   #         break
    #    else:
     #       print("Ping")
      #  time.sleep(1)

#def treat_ping_worker(masterManager, server):
 #   while True:
  #      if event.is_set():
   #         break
    #    else:
     #       response = os.system("ping -c 1 "+masterManager.getMaster())
      #      if (response != 0):
       #         server.removeWorker(sys.argv[1])
        #        masterManager.setMaster('http://localhost:'+sys.argv[1])
        #time.sleep(1)

masterManager = masterManagerFunctions.MasterManagerFunctions()
logging.basicConfig(level=logging.INFO)

if (len(sys.argv) == 1):
    node="master"
    
    masterManager.setMaster('http://localhost:9000')
    
    server = SimpleXMLRPCServer(('localhost', 9000), logRequests=True)

    #name_thread = threading.Thread(target=treat_ping_master, args=())
else:
    node="worker"
    
    proxy = xmlrpc.client.ServerProxy(masterManager.getMaster())
    proxy.addWorker('http://localhost:'+sys.argv[1])

    server = SimpleXMLRPCServer(('localhost', int(sys.argv[1])), logRequests=True)

    #name_thread = threading.Thread(target=treat_ping_worker, args=(masterManager, server))

server.register_instance(workerFunctions.WorkerFunctions())

try:
    print('Use control + c to exit the '+node+' node.')
    #event = threading.Event()
    #name_thread.start()
    server.serve_forever()
except KeyboardInterrupt:
    print('Exiting '+node+' node...')
    #event.set()
    #name_thread.join()
    if (len(sys.argv) == 2):
        proxy.removeWorker(sys.argv[1])