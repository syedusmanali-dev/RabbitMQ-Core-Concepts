#!/usr/bin/env python
import pika
import sys
import os
import time

def main():

    # ✅ Add credentials (IMPORTANT — fixes ACCESS_REFUSED issue)
    credentials = pika.PlainCredentials('hello', 'hello')

    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host='localhost',
            port=5672,
            credentials=credentials
        )
    )

    channel = connection.channel()

    # ⚠️ quorum queues require RabbitMQ 3.8+ and correct setup
    channel.queue_declare(
        queue='hello',
        durable=True
    )

    def callback(ch, method, properties, body):
        print(f" [x] Received {body.decode()}")
        ch.basic_ack(delivery_tag=method.delivery_tag)  # safer than auto_ack

    # ❗ auto_ack=True is NOT recommended for production
    channel.basic_consume(
        queue='hello',
        on_message_callback=callback
    )

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)