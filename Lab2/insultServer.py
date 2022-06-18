from xmlrpc.server import SimpleXMLRPCServer
import logging
import random
import os

server = SimpleXMLRPCServer(('localhost', 9000), logRequests=True)
logging.basicConfig(level=logging.INFO)

insults=[]

def addInsult(insult):
    insults.append(insult)
    return ' '

server.register_function(addInsult)

def getInsults():
    return list(insults)

server.register_function(getInsults)

def insultme():
    return random.choice(insults)

server.register_function(insultme)

try:
    print('Use control + c to exit')
    server.serve_forever()
except KeyboardInterrupt:
    print('Exiting')