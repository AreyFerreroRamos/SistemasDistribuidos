import redis
import xmlrpc.client
import threading
import sys

redis_cli = redis.Redis(host="localhost", port=16379, decode_responses=True, encoding="utf-8")

def treat_file(client_worker, i, max, mins):
    print(client_worker.readCSV(sys.argv[i])+"\n")
    print(client_worker.columns()+"\n")
    print(client_worker.head(5)+"\n")
    print(client_worker.isin('City', 'Tarragona')+"\n")
    print(client_worker.item(5, 3)+"\n")
    maxs.append(float(client_worker.max('Temp_max')))
    mins.append(float(client_worker.min('Temp_min')))

threads=[]
maxs=[]
mins=[]

i=1
while i<len(sys.argv):
    num_worker=0
    while num_worker<redis_cli.llen('workers') and i<len(sys.argv):
        worker = redis_cli.lpop('workers')
        client_worker = xmlrpc.client.ServerProxy(worker)
        threads.append(threading.Thread(target=treat_file, name="thread%s" %i, args=(client_worker, i, maxs, mins)))
        threads[num_worker].start()
        num_worker+=1
        i+=1
        redis_cli.rpush('workers', worker)
    num_worker=0
    while num_worker<len(threads):
        threads[num_worker].join()
        num_worker+=1
    threads.clear()

print("Temperatura maxima: "+str(max(maxs)))
print("Temperatura minima: "+str(min(mins)))