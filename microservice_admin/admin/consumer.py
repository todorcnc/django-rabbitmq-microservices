import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")

import django
django.setup()

import pika
import json

from admin.api.models import Product

connection = pika.BlockingConnection(pika.URLParameters('amqps://tpedvdlf:Kzy6nHXulkOmJVqN3GpNwzLCl1V-Gm-X@cow.rmq2.cloudamqp.com/tpedvdlf'))

channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print('Received in Admin')
    data = json.loads(body)
    print(data)
    print(properties.content_type)

    if properties.content_type == 'product_created':
        product = Product(id=data['id'], title = data['title'], image = data['image'])
        product.save()
        print("Product created from Consumer in Admin")

    elif properties.content_type == 'product_updated':
        product = Product.objects.get(id=data['id'])
        product.title = data['title']
        product.image = data['image']
        product.save()
        print("Product updated from Consumer in Admin")

    elif properties.content_type == 'product_deleted':
        product = Product.objects.get(id=int(data))
        product.delete()
        print("Product deleted from Consumer in Admin")

channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('Started Consuming.....')

channel.start_consuming()

channel.close()