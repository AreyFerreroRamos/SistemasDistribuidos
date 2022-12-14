import redis

class WorkerFunctions:
    redis_cli = redis.Redis(host="localhost", port=16379, decode_responses=True, encoding="utf-8")

    def addWorker(self, worker):
        self.redis_cli.rpush('workers', worker)
        return ' '

    def getWorker(self):
        return self.redis_cli.lpop('workers')

    def numWorkers(self):
        return self.redis_cli.llen('workers')

    def removeWorker(self, port):
        self.redis_cli.lrem('workers', 0, 'http://localhost:'+port)
        return ' '