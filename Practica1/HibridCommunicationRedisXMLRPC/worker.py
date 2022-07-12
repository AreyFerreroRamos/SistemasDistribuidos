import redis
from xmlrpc.server import SimpleXMLRPCServer
import logging
import sys
import daskFunctions

redis_cli = redis.Redis(host="localhost", port=16379)
redis_cli.rpush('workers', 'http://localhost:'+sys.argv[1])

worker = SimpleXMLRPCServer(('localhost', int(sys.argv[1])), logRequests=True)
logging.basicConfig(level=logging.INFO)

worker.register_instance(daskFunctions.DaskFunctions())

try:
    print('Use control + c to exit the Worker node')
    worker.serve_forever()
except KeyboardInterrupt:
    print('Exiting Worker node')
    redis_cli.lrem('workers', 0, 'http://localhost:'+sys.argv[1])