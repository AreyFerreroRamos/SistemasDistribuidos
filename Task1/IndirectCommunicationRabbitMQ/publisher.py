import pika

class Publisher:
    def __init__(self, config):
        self.config = config
        self.connection = self.create_connection()

    def __del__(self):
        self.connection.close()

    def create_connection(self):
        return pika.BlockingConnection(pika.ConnectionParameters(host=self.config['host'], port=self.config['port']))

    def publish(self, routing_key, message):
        channel = self.connection.channel()

        channel.exchange_declare(exchange='workers', exchange_type='topic')

        channel.basic_publish(exchange='workers', routing_key=routing_key, body=message)
        print(" [x] Sent message from %r" % (routing_key))