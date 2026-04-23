import sys
import pika

def main():

    message = ' '.join(sys.argv[1:]) or "Hello World!"

    credentials = pika.PlainCredentials('hello', 'hello')

    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host='localhost',
            port=5672,
            credentials=credentials
        )
    )

    channel = connection.channel()

    channel.queue_declare(queue='hello', durable=True)

    channel.basic_publish(
        exchange='',
        routing_key='hello',
        body=message
    )

    print(f" [x] Sent {message}")

    connection.close()


if __name__ == "__main__":
    main()