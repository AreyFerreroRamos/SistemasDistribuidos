import redis

redis_cli = redis.Redis(host="localhost", port=16379, decode_responses=True, encoding="utf-8")
redis_cli.set('num_workers', str(0))