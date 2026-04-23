import pika
import uuid

credentials = pika.PlainCredentials('hello', 'hello')

connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host='localhost',
        port=5672,
        credentials=credentials
    )
)

channel = connection.channel()

# 🔥 create temporary reply queue
result = channel.queue_declare(queue='', exclusive=True)
callback_queue = result.method.queue

corr_id = str(uuid.uuid4())
response = None

def on_response(ch, method, props, body):
    global response
    if props.correlation_id == corr_id:
        response = body

channel.basic_consume(
    queue=callback_queue,
    on_message_callback=on_response,
    auto_ack=True
)

# 🔥 send request
n = 5
channel.basic_publish(
    exchange='',
    routing_key='rpc_queue',
    properties=pika.BasicProperties(
        reply_to=callback_queue,
        correlation_id=corr_id
    ),
    body=str(n)
)

print(f" [x] Requesting fib({n})")

# 🔥 wait for response
while response is None:
    connection.process_data_events()

print(f" [.] Got result: {response.decode()}")