import pika

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

    # 🔥 Same exchange
    channel.exchange_declare(exchange='logs', exchange_type='fanout')

    # ⚡ Create RANDOM queue (important for pub-sub)
    result = channel.queue_declare(queue='', exclusive=True)
    queue_name = result.method.queue

    # 🔗 Bind queue to exchange
    channel.queue_bind(exchange='logs', queue=queue_name)

    print(' [*] Waiting for logs. To exit press CTRL+C')

    def callback(ch, method, properties, body):
        print(f" [x] Received {body.decode()}")

    channel.basic_consume(
        queue=queue_name,
        on_message_callback=callback,
        auto_ack=True
    )

    channel.start_consuming()


if __name__ == "__main__":
    main()