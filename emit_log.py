import pika
import sys

def main():

    credentials = pika.PlainCredentials('hello', 'hello')

    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host='localhost',
            port=5672,
            credentials=credentials
        )
    )

    channel = connection.channel()

    # 🔥 Create FANOUT exchange
    channel.exchange_declare(exchange='logs', exchange_type='fanout')

    message = ' '.join(sys.argv[1:]) or "info: Hello World!"

    # ❗ No routing_key needed in fanout
    channel.basic_publish(
        exchange='logs',
        routing_key='',
        body=message
    )

    print(f" [x] Sent {message}")

    connection.close()


if __name__ == "__main__":
    main()