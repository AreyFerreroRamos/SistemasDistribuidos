import redis
import daskFunctions
import time

redis_cli = redis.Redis(host="localhost", port=16379, decode_responses=True, encoding="utf-8")

num_worker = redis_cli.get('num_workers')
redis_cli.set('num_workers', str(int(num_worker)+1))

pubsub_name_file = redis_cli.pubsub()
pubsub_name_file.subscribe('worker'+num_worker)

pubsub_restructure_nodes = redis_cli.pubsub()
pubsub_restructure_nodes.subscribe('restructure_nodes'+num_worker)

worker = daskFunctions.DaskFunctions()

try:
    print('Use control + c to exit the Worker node.')
    while True:
        message = pubsub_name_file.get_message(ignore_subscribe_messages=True)
        if message and (message.get('type') == "message"):
            redis_cli.publish(message.get('data'), worker.readCSV(message.get('data')))
            redis_cli.publish(message.get('data'), worker.columns())
            redis_cli.publish(message.get('data'), worker.head(5))
            redis_cli.publish(message.get('data'), worker.isin('City', 'Tarragona'))
            redis_cli.publish(message.get('data'), worker.item(5, 3))
            redis_cli.publish(message.get('data'), worker.max('Temp_max'))
            redis_cli.publish(message.get('data'), worker.min('Temp_min'))
        message_restructure = pubsub_restructure_nodes.get_message(ignore_subscribe_messages=True)
        if message_restructure and (message_restructure.get('type') == "message"):
            if int(message_restructure.get('data')) < int(num_worker):
                pubsub_name_file.unsubscribe('worker'+num_worker)
                pubsub_restructure_nodes.unsubscribe('restructure_nodes'+num_worker)
                num_worker=str(int(num_worker)-1)
                pubsub_name_file.subscribe('worker'+num_worker)
                pubsub_restructure_nodes.subscribe('restructure_nodes'+num_worker)
        time.sleep(1)
except KeyboardInterrupt:
    print('Exiting worker node.')
    pubsub_name_file.unsubscribe('worker'+num_worker)
    pubsub_restructure_nodes.unsubscribe('worker'+num_worker)
    i=0
    while i<int(redis_cli.get('num_workers')):
        if i != num_worker:
            redis_cli.publish('restructure_nodes'+str(i), str(num_worker))
        i+=1
    redis_cli.set('num_workers', str(int(redis_cli.get('num_workers'))-1))