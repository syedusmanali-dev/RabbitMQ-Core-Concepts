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

    # 🔥 Topic exchange
    channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

    routing_key = sys.argv[1] if len(sys.argv) > 1 else 'info.general'
    message = ' '.join(sys.argv[2:]) or 'Hello Topic!'

    channel.basic_publish(
        exchange='topic_logs',
        routing_key=routing_key,
        body=message
    )

    print(f" [x] Sent [{routing_key}] {message}")

    connection.close()


if __name__ == "__main__":
    main()