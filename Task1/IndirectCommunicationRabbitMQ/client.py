import publisher
import consumer
import sys
     
class ConsumerClient(consumer.Consumer):
    def callback(self, channel, method, properties, body):
        print(" [x] Received new message.\n")
        print(body.decode().split(':')[0]+'\n')
        print(body.decode().split(':')[1]+'\n')
        print(body.decode().split(':')[2]+'\n')
        print(body.decode().split(':')[3]+'\n')
        print(body.decode().split(':')[4]+'\n')
        maxs.append(float(body.decode().split(':')[5]))
        mins.append(float(body.decode().split(':')[6]))

maxs=[]
mins=[]

publisher_name = publisher.Publisher({'host': 'localhost', 'port': 5672})

i=1
while i<len(sys.argv):
    publisher_name.publish('workers', 'worker', sys.argv[i]+':'+str(5)+':'+'City'+':'+'Tarragona'+':'+str(5)+':'+str(3))
    i+=1

consumer_file = ConsumerClient({'host':'localhost', 'port':5672, 'timeout':3}, 'client', 'proves')
consumer_file.consume()

print("Temperatura maxima: "+str(max(maxs)))
print("Temperatura minima: "+str(min(mins)))