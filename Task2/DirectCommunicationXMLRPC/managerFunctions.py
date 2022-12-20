import redis

class ManagerFunctions:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self):
        self.redis_cli = redis.Redis(host="localhost", port=16379, decode_responses=True, encoding="utf-8")

    def setMaster(self, master):
        self.redis_cli.set('master', master)
        return ' '

    def getMaster(self):
        return self.redis_cli.get('master')

    def addWorker(self, worker):
        self.redis_cli.rpush('workers', worker)
        return ' '

    def getWorker(self):
        return self.redis_cli.lpop('workers')

    def listWorkers(self):
        return self.redis_cli.lrange('workers', 0, -1)

    def numWorkers(self):
        return self.redis_cli.llen('workers')

    def removeWorker(self, port):
        self.redis_cli.lrem('workers', 0, 'http://localhost:'+port)
        return ' '