import redis
import sys
import time

redis_cli = redis.Redis(host="localhost", port=16379, decode_responses=True, encoding="utf-8")
pubsub = redis_cli.pubsub()

maxs=[]
mins=[]
i=1

while i<len(sys.argv):
    redis_cli.publish('worker'+str(i%int(redis_cli.get('num_workers'))), sys.argv[i])
    pubsub.subscribe(sys.argv[i])
    capturate=False
    while not capturate:
        message = pubsub.get_message(ignore_subscribe_messages=True)
        if message and (message.get('type') == 'message'):
            print(message.get('data')+"\n")
            print(pubsub.get_message(ignore_subscribe_messages=True).get('data')+"\n")
            redis_cli.publish('worker'+str(i%int(redis_cli.get('num_workers'))), str(5))
            while not capturate:
                head = pubsub.get_message(ignore_subscribe_messages=True)
                if head and (head.get('type') == "message"):
                    print(head.get('data')+"\n")
                    capturate = True
                else:
                    time.sleep(0.1)
            redis_cli.publish('worker'+str(i%int(redis_cli.get('num_workers'))), 'City')
            redis_cli.publish('worker'+str(i%int(redis_cli.get('num_workers'))), 'Tarragona')
            capturate = False
            while not capturate:
                isin = pubsub.get_message(ignore_subscribe_messages=True)
                if isin and (isin.get('type') == "message"):
                    print(isin.get('data')+"\n")
                    capturate = True
                else:
                    time.sleep(0.1)
            maxs.append(float(pubsub.get_message(ignore_subscribe_messages=True).get('data')))
            mins.append(float(pubsub.get_message(ignore_subscribe_messages=True).get('data')))
            pubsub.unsubscribe(sys.argv[i])
            capturate = True
        else:
            time.sleep(0.1)
    i+=1

print("Temperatura maxima: "+str(max(maxs)))
print("Temperatura minima: "+str(min(mins)))