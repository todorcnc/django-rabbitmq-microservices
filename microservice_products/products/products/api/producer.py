import pika
import json

connection = pika.BlockingConnection(pika.URLParameters('amqps://tpedvdlf:Kzy6nHXulkOmJVqN3GpNwzLCl1V-Gm-X@cow.rmq2.cloudamqp.com/tpedvdlf'))

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)