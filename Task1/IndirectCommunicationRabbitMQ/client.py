import publisher
import pika
import sys
     
class ConsumerClient:
    def __init__(self, config, queue_name, binding_key):
        self.config = config
        self.queue_name = queue_name
        self.binding_key = binding_key
        self.connection = self.create_connection()

    def __del__(self):
        self.connection.close()

    def create_connection(self):
        return pika.BlockingConnection(pika.ConnectionParameters(host=self.config['host'], port=self.config['port']))

    def callback(self, channel, method, properties, body):
        print(" [x] Received new message from %r" % (method.routing_key)+'\n')
        
        print(body.decode().split(':')[0]+'\n')
        print(body.decode().split(':')[1]+'\n')
        print(body.decode().split(':')[2]+'\n')
        print(body.decode().split(':')[3]+'\n')
        print(body.decode().split(':')[4]+'\n')
        maxs.append(float(body.decode().split(':')[5]))
        mins.append(float(body.decode().split(':')[6]))

    def consume(self):
        channel = self.connection.channel()

        channel.exchange_declare(exchange='workers', exchange_type='topic')
        channel.queue_declare(queue=self.queue_name, exclusive=True)
        channel.queue_bind(exchange='workers', queue=self.queue_name, routing_key=self.binding_key)

        channel.basic_consume(queue=self.queue_name, on_message_callback=self.callback, auto_ack=True)

        try:
            print(' [*] Waiting for data for '+self.queue_name+'. Use control + c to exit the Client')
            channel.start_consuming()
        except KeyboardInterrupt:
            print(' [*] Exiting client')
            channel.stop_consuming()

maxs=[]
mins=[]
i=1

publisher_name = publisher.Publisher({'host': 'localhost', 'port': 5672})

while i<len(sys.argv):
    publisher_name.publish('worker'+'1', sys.argv[i]+':'+str(5)+':'+'City'+':'+'Tarragona'+':'+str(5)+':'+str(3))
    i+=1

consumer_file = ConsumerClient({'host':'localhost', 'port':5672}, 'proves', 'proves')
consumer_file.consume()

print("Temperatura maxima: "+str(max(maxs)))
print("Temperatura minima: "+str(min(mins)))