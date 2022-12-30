from xmlrpc.server import SimpleXMLRPCServer
import threading
import logging
import sys
import nodeType
import manageNodes
import serverFunctions

node = nodeType.NodeType("master")

master = SimpleXMLRPCServer(('localhost', int(sys.argv[1])), logRequests=True, allow_none=True)
logging.basicConfig(level=logging.INFO)
master.register_instance(serverFunctions.ServerFunctions('http://localhost:'+sys.argv[1]))

event = threading.Event()
name_thread = threading.Thread(target=manageNodes.pingNodes, args=(node, sys.argv[1], event,))

try:
    print('Use control + c to exit the '+node.getNodeType()+' node.')
    name_thread.start()
    master.serve_forever()
except KeyboardInterrupt:
    print('Exiting '+node.getNodeType()+' node...')
    event.set()
    name_thread.join()