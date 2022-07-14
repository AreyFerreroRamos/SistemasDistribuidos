import redis
import sys

redis_cli = redis.Redis(host="localhost", port=16379)

#maxs=[]
#mins=[]
i=1

while i<len(sys.argv):
    print(sys.argv[i])
    redis_cli.publish('read_csv', sys.argv[i])
    #print(client_worker.readCSV(sys.argv[i])+"\n")
    #print(client_worker.columns()+"\n")
    #print(client_worker.head(5)+"\n")
    #print(client_worker.isin('City', 'Tarragona')+"\n")
    #print(client_worker.item(5, 3)+"\n")
    #maxs.append(float(client_worker.max('Temp_max')))
    #mins.append(float(client_worker.min('Temp_min')))
    i+=1

#print("Temperatura maxima: "+str(max(maxs)))
#print("Temperatura minima: "+str(min(mins)))