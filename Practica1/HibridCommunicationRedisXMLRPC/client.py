import redis
import xmlrpc.client
import sys

redis_cli = redis.Redis(host="localhost", port=16379, decode_responses=True, encoding="utf-8")

maxs=[]
mins=[]
i=1

while i<len(sys.argv):
    worker = redis_cli.lpop('workers')
    client_worker = xmlrpc.client.ServerProxy(worker)
    redis_cli.rpush('workers', worker)
    print(client_worker.readCSV(sys.argv[i])+"\n")
    print(client_worker.columns()+"\n")
    print(client_worker.head(5)+"\n")
    print(client_worker.isin('City', 'Tarragona')+"\n")
    print(client_worker.item(5, 3)+"\n")
    maxs.append(float(client_worker.max('Temp_max')))
    mins.append(float(client_worker.min('Temp_min')))
    i+=1

print("Temperatura maxima: "+str(max(maxs)))
print("Temperatura minima: "+str(min(mins)))