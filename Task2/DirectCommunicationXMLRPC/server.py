from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client
import threading
import logging
import sys
import os
import nodeType
import pingNodes
import serverFunctions

node = nodeType.NodeType()
event = threading.Event()

logging.basicConfig(level=logging.INFO)

if (len(sys.argv) == 2):
    node.setNodeType("master")

    server = SimpleXMLRPCServer(('localhost', int(sys.argv[1])), logRequests=True, allow_none=True)
    
    name_thread = threading.Thread(target=pingNodes.ping_nodes, args=(node, sys.argv[1], event,))
else:
    node.setNodeType("worker")

    proxy = xmlrpc.client.ServerProxy('http://localhost:'+sys.argv[1], allow_none=True)
    proxy.addWorker('http://localhost:'+sys.argv[2])
    
    server = SimpleXMLRPCServer(('localhost', int(sys.argv[2])), logRequests=True, allow_none=True)

    name_thread = threading.Thread(target=pingNodes.ping_nodes, args=(node, sys.argv[2], event,))

server.register_instance(serverFunctions.ServerFunctions('http://localhost:'+sys.argv[1]))

try:
    print('Use control + c to exit the '+node.getNodeType()+' node.')
    name_thread.start()
    server.serve_forever()
except KeyboardInterrupt:
    print('Exiting '+node.getNodeType()+' node...')
    event.set()
    name_thread.join()