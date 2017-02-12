#!/bin/env python
import pika

exchange_name = 'temp_direct'
queue_name = 'hello'
route_key = 'lc.2016.12.16'
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost',credentials=pika.PlainCredentials(username='liuchi',password='123456')))
channel = connection.channel()
channel.exchange_declare(exchange=exchange_name,exchange_type='direct',durable=True)
channel.queue_declare(queue=queue_name,durable=False)
channel.queue_bind(queue=queue_name,exchange=exchange_name,routing_key=route_key)
channel.basic_publish(exchange=exchange_name,routing_key=route_key,body='hello world python')