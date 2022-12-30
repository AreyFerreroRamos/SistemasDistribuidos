from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client
import threading
import logging
import sys
import nodeType
import manageNodes
import serverFunctions

node = nodeType.NodeType("worker")

proxy = xmlrpc.client.ServerProxy('http://localhost:'+sys.argv[1], allow_none=True)
proxy.addWorker('http://localhost:'+sys.argv[2])

worker = SimpleXMLRPCServer(('localhost', int(sys.argv[2])), logRequests=True, allow_none=True)
logging.basicConfig(level=logging.INFO)
worker.register_instance(serverFunctions.ServerFunctions('http://localhost:'+sys.argv[1]))

event = threading.Event()
name_thread = threading.Thread(target=manageNodes.pingNodes, args=(node, sys.argv[2], event,))

try:
    print('Use control + c to exit the '+node.getNodeType()+' node.')
    name_thread.start()
    worker.serve_forever()
except KeyboardInterrupt:
    print('Exiting '+node.getNodeType()+' node...')
    event.set()
    name_thread.join()