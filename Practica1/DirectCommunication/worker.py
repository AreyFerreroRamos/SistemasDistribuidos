import xmlrpc.client
import sys
import os

from xmlrpc.server import SimpleXMLRPCServer
import logging
import pandas

proxy = xmlrpc.client.ServerProxy('http://localhost:9000')
proxy.addWorker('http://localhost:'+sys.argv[1])

worker = SimpleXMLRPCServer(('localhost', int(sys.argv[1])), logRequests=True)
logging.basicConfig(level=logging.INFO)

def readCSV(name_file):
    df = pandas.read_csv(name_file)
    return df

def apply():
    return ' '

def columns(name_file):
    df = pandas.read_csv(name_file, usecols=['File','Status'])
    return str(df.columns(2))

def groupby():
    return ' '

def head():
    return ' '

def isin():
    return ' '

def items():
    return ' '

def max():
    return ' '

def min():
    return ' '

worker.register_function(readCSV)
worker.register_function(apply)
worker.register_function(columns)
worker.register_function(groupby)
worker.register_function(head)
worker.register_function(isin)
worker.register_function(items)
worker.register_function(max)
worker.register_function(min)

try:
    print('Use control + c to exit the Worker node')
    worker.serve_forever()
except KeyboardInterrupt:
    print('Exiting Worker node')
    proxy.removeWorker(sys.argv[1])