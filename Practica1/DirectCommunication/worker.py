from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client
import logging
import sys
import os
import pandas
import dask.dataframe as dd

proxy = xmlrpc.client.ServerProxy('http://localhost:9000')

proxy.addWorker('http://localhost:'+sys.argv[1])

worker = SimpleXMLRPCServer(('localhost', sys.argv[1]), logRequests=True)
logging.basicConfig(level=logging.INFO)

def readCSV(name_file):
    file = dd.read_csv(name_file)
    return file

def min():
    return ' '

worker.register_function(readCSV)
worker.register_function(min)

try:
    print('Use control + c to exit the Worker node')
    worker.serve_forever()
except KeyboardInterrupt:
    print('Exiting Worker node')
    proxy.removeWorker(sys.argv[1])