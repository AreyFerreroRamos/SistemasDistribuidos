import redis
import daskFunctions
import time

redis_cli = redis.Redis(host="localhost", port=16379, decode_responses=True, encoding="utf-8")
pubsub_name_file = redis_cli.pubsub()
pubsub_name_file.subscribe('name_file')

worker = daskFunctions.DaskFunctions()

try:
    print('Use control + c to exit the Worker node.')
    while True:
        message = pubsub_name_file.get_message(ignore_subscribe_messages=True)
        if message and (message.get('type') == "message"):
            redis_cli.publish(message.get('data'), worker.readCSV(message.get('data')))
        time.sleep(1)
except KeyboardInterrupt:
    print('Exiting worker node.')
    pubsub_name_file.unsubscribe('name_file')