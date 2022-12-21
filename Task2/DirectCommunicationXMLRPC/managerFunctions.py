import redis

class ManagerFunctions:
    def __init__(self):
        self.redis_cli = redis.Redis(host="localhost", port=16379, decode_responses=True, encoding="utf-8")
        self.node_type = ""

    def setMaster(self, master):
        self.redis_cli.set('master', master)
        return ' '

    def getMaster(self):
        return self.redis_cli.get('master')

    def setNodeType(self, node_type):
        self.node_type = node_type
    
    def getNodeType(self):
        return self.node_type