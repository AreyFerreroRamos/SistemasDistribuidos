from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client
import logging
import sys
import workerFunctions
import daskFunctions

if (len(sys.argv) == 1):
    master = SimpleXMLRPCServer(('localhost', 9000), logRequests=True)
    logging.basicConfig(level=logging.INFO)

    master.register_instance(workerFunctions.WorkerFunctions())

    try:
        print('Use control + c to exit the Master node')
        master.serve_forever()
    except KeyboardInterrupt:
        print('Exiting master node')
else:
    proxy = xmlrpc.client.ServerProxy('http://localhost:9000')
    proxy.addWorker('http://localhost:'+sys.argv[1])

    worker = SimpleXMLRPCServer(('localhost', int(sys.argv[1])), logRequests=True)
    logging.basicConfig(level=logging.INFO)

    worker.register_instance(daskFunctions.DaskFunctions())

    try:
        print('Use control + c to exit the Worker node')
        worker.serve_forever()
    except KeyboardInterrupt:
        print('Exiting Worker node')
        proxy.removeWorker(sys.argv[1])