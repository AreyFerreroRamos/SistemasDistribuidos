import redis
import sys
import time

redis_cli = redis.Redis(host="localhost", port=16379, decode_responses=True, encoding="utf-8")
pubsub_read_file = redis_cli.pubsub()

maxs=[]
mins=[]
i=1

while i<len(sys.argv):
    redis_cli.publish('worker'+str(i%int(redis_cli.get('num_workers'))), sys.argv[i])
    pubsub_read_file.subscribe(sys.argv[i])
    capturate=False
    while not capturate:
        message = pubsub_read_file.get_message(ignore_subscribe_messages=True)
        if message and (message.get('type') == 'message'):
            print(message.get('data')+"\n")
            maxs.append(float(pubsub_read_file.get_message(ignore_subscribe_messages=True).get('data')))
            mins.append(float(pubsub_read_file.get_message(ignore_subscribe_messages=True).get('data')))
            pubsub_read_file.unsubscribe(sys.argv[i])
            capturate = True
        else:
            time.sleep(1)
    i+=1

print("Temperatura maxima: "+str(max(maxs)))
print("Temperatura minima: "+str(min(mins)))