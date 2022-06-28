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
    return str(df)

def columns(name_file, field):
    df = pandas.read_csv(name_file)
    return str(df.loc[:,field])

def groupby(name_file, field):
    df = pandas.read_csv(name_file)
    return str(df.groupby(field))

def head(name_file, num_rows):
    df = pandas.read_csv(name_file)
    return str(df.head(num_rows))

def isin(name_file, field, min, max):
    df = pandas.read_csv(name_file)
    return str(df.isin({field: [min, max]}))

def items(name_file):
    df = pandas.read_csv(name_file)
    return str(df.items())

def max(name_file, field):
    df = pandas.read_csv(name_file)
    return str(df.loc[:,field].max())

def min(name_file, field):
    df = pandas.read_csv(name_file)
    return str(df.loc[:,field].min())

worker.register_function(readCSV)
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