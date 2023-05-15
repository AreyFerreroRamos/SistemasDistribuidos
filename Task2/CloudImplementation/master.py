from xmlrpc.server import SimpleXMLRPCServer
import logging
import workerFunctions

master = SimpleXMLRPCServer(('localhost', 9000), logRequests=True)
logging.basicConfig(level=logging.INFO)

master.register_instance(workerFunctions.WorkerFunctions())

try:
    print('Use control + c to exit the Master node')
    master.serve_forever()
except KeyboardInterrupt:
    print('Exiting master node')