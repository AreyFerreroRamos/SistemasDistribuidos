import redis
import daskFunctions
import time

print('Use control + c to exit the Worker node.')
redis_cli = redis.Redis(host="localhost", port=16379)
pubsub = redis_cli.pubsub()
pubsub.subscribe('read_csv')
worker = daskFunctions.DaskFunctions()

try:
    while True:
        message = pubsub.get_message()
        if message:
            print("Hem entrat al cos del if.")
            print(message)
            print(worker.readCSV(message))
        time.sleep(86400)
except KeyboardInterrupt:
    print('Exiting worker node')
    pubsub.unsubscribe('read_csv')