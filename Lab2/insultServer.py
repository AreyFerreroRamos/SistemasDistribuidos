from xmlrpc.server import SimpleXMLRPCServer
import random

with SimpleXMLRPCServer((localhost, 8000), requestHandler=RequestHandler) as server:
    server.register_functions() 

insults=[]

def addInsult(insult):
    insults.append(insult)

server.register_functions(addInsult)

def getInsults():
    return list(insults)

server.register_functions(getInsults)

def insultme():
    return random.choice(insults)

server.register_functions(insultme)
