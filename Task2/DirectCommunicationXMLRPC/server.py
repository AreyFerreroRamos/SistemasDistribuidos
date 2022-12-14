from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client
import logging
import sys
import workerFunctions
import daskFunctions

logging.basicConfig(level=logging.INFO)

if (len(sys.argv) == 1):
    node="master"
    server = SimpleXMLRPCServer(('localhost', 9000), logRequests=True)
    server.register_instance(workerFunctions.WorkerFunctions())
else:
    node="worker"
    proxy = xmlrpc.client.ServerProxy('http://localhost:9000')
    proxy.addWorker('http://localhost:'+sys.argv[1])

    server = SimpleXMLRPCServer(('localhost', int(sys.argv[1])), logRequests=True)
    server.register_instance(daskFunctions.DaskFunctions())

try:
    print('Use control + c to exit the '+node+' node.')
    server.serve_forever()
except KeyboardInterrupt:
    print('Exiting '+node+' node...')
    if (len(sys.argv) == 2):
        proxy.removeWorker(sys.argv[1])