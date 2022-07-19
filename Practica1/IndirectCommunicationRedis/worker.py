import redis
import daskFunctions
import time

redis_cli = redis.Redis(host="localhost", port=16379, decode_responses=True, encoding="utf-8")

num_worker = redis_cli.get('num_workers')
redis_cli.set('num_workers', str(int(num_worker)+1))

pubsub_dask = redis_cli.pubsub()
pubsub_dask.subscribe('worker'+num_worker)

pubsub_restructure_nodes = redis_cli.pubsub()
pubsub_restructure_nodes.subscribe('restructure_nodes'+num_worker)

worker = daskFunctions.DaskFunctions()

try:
    print('Use control + c to exit the Worker node.')
    while True:
        name_file = pubsub_dask.get_message(ignore_subscribe_messages=True)
        if name_file and (name_file.get('type') == "message"):
            redis_cli.publish(name_file.get('data'), worker.readCSV(name_file.get('data')))
            redis_cli.publish(name_file.get('data'), worker.columns())
            capturate = False
            while not capturate:
                num_rows = pubsub_dask.get_message(ignore_subscribe_messages=True)
                if num_rows and (num_rows.get('type') == "message"):
                    redis_cli.publish(name_file.get('data'), worker.head(int(num_rows.get('data'))))
                    capturate = True
                else:
                    time.sleep(0.1)
            capturate = False
            while not capturate:
                field_element = pubsub_dask.get_message(ignore_subscribe_messages=True)
                if field_element and (field_element.get('type') == "message"):
                    redis_cli.publish(name_file.get('data'), worker.isin(field_element.get('data').split(':')[0], field_element.get('data').split(':')[1]))
                    capturate = True
                else:
                    time.sleep(0.1)
            capturate = False
            while not capturate:
                row_column = pubsub_dask.get_message(ignore_subscribe_messages=True)
                if row_column and (row_column.get('type') == "message"):
                    redis_cli.publish(name_file.get('data'), worker.item(int(row_column.get('data').split(':')[0]), int(row_column.get('data').split(':')[1])))
                    capturate = True
                else:
                    time.sleep(0.1)
            redis_cli.publish(name_file.get('data'), worker.max('Temp_max'))
            redis_cli.publish(name_file.get('data'), worker.min('Temp_min'))
        message_restructure = pubsub_restructure_nodes.get_message(ignore_subscribe_messages=True)
        if message_restructure and (message_restructure.get('type') == "message"):
            if int(message_restructure.get('data')) < int(num_worker):
                pubsub_dask.unsubscribe('worker'+num_worker)
                pubsub_restructure_nodes.unsubscribe('restructure_nodes'+num_worker)
                num_worker=str(int(num_worker)-1)
                pubsub_dask.subscribe('worker'+num_worker)
                pubsub_restructure_nodes.subscribe('restructure_nodes'+num_worker)
        time.sleep(0.1)
except KeyboardInterrupt:
    print('Exiting worker node.')
    pubsub_dask.unsubscribe('worker'+num_worker)
    pubsub_restructure_nodes.unsubscribe('worker'+num_worker)
    i=0
    while i<int(redis_cli.get('num_workers')):
        if i != num_worker:
            redis_cli.publish('restructure_nodes'+str(i), str(num_worker))
        i+=1
    redis_cli.set('num_workers', str(int(redis_cli.get('num_workers'))-1))