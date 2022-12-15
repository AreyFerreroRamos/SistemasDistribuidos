import redis

class MasterManagerFunctions:
    redis_cli = redis.Redis(host="localhost", port=16379, decode_responses=True, encoding="utf-8")

    def setMaster(self, master):
        self.redis_cli.set('master', master)
        return ' '

    def getMaster(self):
        return self.redis_cli.get('master')