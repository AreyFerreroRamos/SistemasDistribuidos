import pika
import sys

class PublisherClient:
    def __init__(self, config):
        self.config = config
        self.connection = self.create_connection()

    def __del__(self):
        self.connection.close()

    def create_connection(self):
        return pika.BlockingConnection(pika.ConnectionParameters(host=self.config['host'], port=self.config['port']))

    def publish(self, routing_key, message):
        channel = self.connection.channel()

        channel.exchange_declare(exchange='proves', exchange_type='topic')

        channel.basic_publish(exchange='proves', routing_key=routing_key, body=message)
        print(" [x] Sent message %r from %r" % (message, routing_key))
        
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
        print(" [x] Received new message from %r" % (method.routing_key))
        print(body.decode())

    def consume(self):
        channel = self.connection.channel()

        channel.exchange_declare(exchange='proves', exchange_type='topic')
        channel.queue_declare(queue=self.queue_name, exclusive=True)
        channel.queue_bind(exchange='proves', queue=self.queue_name, routing_key=self.binding_key)

        channel.basic_consume(queue=self.queue_name, on_message_callback=self.callback, auto_ack=True)

        try:
            print(' [*] Waiting for data for '+self.queue_name+'. Use control + c to exit the Client')
            channel.start_consuming()
        except KeyboardInterrupt:
            print(' [*] Exiting client')
            channel.stop_consuming()

publisher_name = PublisherClient({'host': 'localhost', 'port': 5672})

#maxs=[]
#mins=[]

i=1
while i<len(sys.argv):
    publisher_name.publish('worker'+str(i), sys.argv[i])
    i+=1

i=1    
while i<len(sys.argv):
    consumer_file = ConsumerClient({'host':'localhost', 'port':5672}, sys.argv[i], sys.argv[i])
    consumer_file.consume()     # Se queda atascado en este punto del programa.
    i+=1