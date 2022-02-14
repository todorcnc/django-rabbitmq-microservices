import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "products.settings")

import django
django.setup()

import pika
import json

from products.api.models import Product


connection = pika.BlockingConnection(pika.URLParameters('amqps://tpedvdlf:Kzy6nHXulkOmJVqN3GpNwzLCl1V-Gm-X@cow.rmq2.cloudamqp.com/tpedvdlf'))

channel = connection.channel()

channel.queue_declare(queue='products')

def callback(ch, method, properties, body):
    print('Received in Products')
    product_id = json.loads(body)
    print(properties.content_type)

    if properties.content_type == 'product_liked':
        product = Product.objects.get(id=product_id)
        product.likes = product.likes + 1
        product.save()
        print(f"Product with id:{product_id} was liked in Admin.")



channel.basic_consume(queue='products', on_message_callback=callback, auto_ack=True)

print('Started Consuming.....')

channel.start_consuming()

channel.close()