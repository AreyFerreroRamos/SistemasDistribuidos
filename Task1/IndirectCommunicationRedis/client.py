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
            while not capturate:
                columns = pubsub.get_message(ignore_subscribe_messages=True)
                if columns and (columns.get('type') == "message"):
                    print(columns.get('data')+"\n")
                    capturate = True
                else:
                    time.sleep(0.1)
            redis_cli.publish('worker'+str(i%int(redis_cli.get('num_workers'))), str(5))
            capturate = False
            while not capturate:
                head = pubsub.get_message(ignore_subscribe_messages=True)
                if head and (head.get('type') == "message"):
                    print(head.get('data')+"\n")
                    capturate = True
                else:
                    time.sleep(0.1)
            redis_cli.publish('worker'+str(i%int(redis_cli.get('num_workers'))), 'City'+':'+'Tarragona')
            capturate = False
            while not capturate:
                isin = pubsub.get_message(ignore_subscribe_messages=True)
                if isin and (isin.get('type') == "message"):
                    print(isin.get('data')+"\n")
                    capturate = True
                else:
                    time.sleep(0.1)
            redis_cli.publish('worker'+str(i%int(redis_cli.get('num_workers'))), str(5)+':'+str(3))
            capturate = False
            while not capturate:
                item = pubsub.get_message(ignore_subscribe_messages=True)
                if item and (item.get('type') == "message"):
                    print(item.get('data')+"\n")
                    capturate = True
                else:
                    time.sleep(0.1)
            capturate = False
            while not capturate:
                maxm = pubsub.get_message(ignore_subscribe_messages=True)
                if maxm and (maxm.get('type') == "message"):
                    maxs.append(float(maxm.get('data')))
                    capturate = True
                else:
                    time.sleep(0.1)
            capturate = False
            while not capturate:
                minm = pubsub.get_message(ignore_subscribe_messages=True)
                if minm and (minm.get('type') == "message"):    
                    mins.append(float(minm.get('data')))
                    capturate = True
                else:
                    time.sleep(0.1)
            pubsub.unsubscribe(sys.argv[i])
        else:
            time.sleep(0.1)
    i+=1

print("Temperatura maxima: "+str(max(maxs)))
print("Temperatura minima: "+str(min(mins)))