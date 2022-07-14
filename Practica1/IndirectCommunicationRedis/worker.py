import redis
import daskFunctions

print('Use control + c to exit the Worker node.')
worker = daskFunctions.DaskFunctions()
redis_cli = redis.Redis(host="localhost", port=16379)
pubsub = redis_cli.pubsub()
pubsub.subscribe('read_csv')
message = pubsub.get_message()
if message:
    print(message)
    print(worker.readCSV(message))