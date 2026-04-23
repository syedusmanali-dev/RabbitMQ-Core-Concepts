#!/usr/bin/env python
import pika

def main():

    # ✅ FIX 1: Add credentials (required for Docker RabbitMQ)
    credentials = pika.PlainCredentials('hello', 'hello')

    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host='localhost',
            port=5672,
            credentials=credentials
        )
    )

    channel = connection.channel()

    # ✅ FIX 2: Remove quorum config (safe default queue)
    channel.queue_declare(
        queue='hello',
        durable=True
    )

    # Publish message
    channel.basic_publish(
        exchange='',
        routing_key='hello',
        body='Hello World!'
    )

    print(" [x] Sent 'Hello World!'")

    connection.close()


if __name__ == "__main__":
    main()