import xmlrpc.client
import sys

client = xmlrpc.client.ServerProxy('http://localhost:'+sys.argv[1])

