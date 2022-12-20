from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client
#import threading
import logging
import time
import sys
import os
import masterManagerFunctions
import workerFunctions

#def treat_ping_master():
 #   masterManager = masterManagerFunctions.MasterManagerFunctions()
  #  client_master = xmlrpc.client.ServerProxy(masterManager.getMaster())
   # 
    #while True:
     #   time.sleep(5)
      #  if event.is_set():
       #     break
        #else:
         #   for worker in client_master.listWorkers():
          #      response = os.system("ping -c 1 "+worker.split(':')[2]+" "+worker.split(':')[1].split('/')[2])
           #     if (response != 0):
            #        client_master.removeWorker(worker.split(':')[2])

#def treat_ping_worker():
 #   while True:
  #      if event.is_set():
   #         break
    #    else:
     #       response = os.system("ping -c 1 "+masterManager.getMaster())
      #      if (response != 0):
       #         server.removeWorker(sys.argv[1])
        #        masterManager.setMaster('http://localhost:'+sys.argv[1])
         #   time.sleep(1)

masterManager = masterManagerFunctions.MasterManagerFunctions()
logging.basicConfig(level=logging.INFO)

if (len(sys.argv) == 1):
    node="master"
    
    masterManager.setMaster('http://localhost:9000')
    
    server = SimpleXMLRPCServer(('localhost', 9000), logRequests=True)
    
    #name_thread = threading.Thread(target=treat_ping_master)
else:
    node="worker"
    
    proxy = xmlrpc.client.ServerProxy(masterManager.getMaster())
    proxy.addWorker('http://localhost:'+sys.argv[1])

    server = SimpleXMLRPCServer(('localhost', int(sys.argv[1])), logRequests=True)

    #name_thread = threading.Thread(target=treat_ping_worker)

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