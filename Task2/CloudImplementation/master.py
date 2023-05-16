from xmlrpc.server import SimpleXMLRPCServer
import logging
import masterFunctions

master = SimpleXMLRPCServer(('localhost', 9000), logRequests=True)
logging.basicConfig(level=logging.INFO)

master.register_instance(masterFunctions.MasterFunctions())

try:
    print('Use control + c to exit the Master node')
    master.serve_forever()
except KeyboardInterrupt:
    print('Exiting master node')