import daskFunctions
import consumer
import sys

consumer_name = consumer.Consumer({'host':'localhost', 'port':5672}, 'worker'+sys.argv[1], 'worker'+sys.argv[1])
consumer_name.consume()