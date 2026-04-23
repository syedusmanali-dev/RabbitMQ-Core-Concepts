#   🚀 RabbitMQ Hands-On Project (AMQP Practice)

This repository contains my hands-on learning and implementation of RabbitMQ using Python (pika library).
It covers core messaging concepts used in real-world distributed systems, microservices, and AI pipelines.

#   📚 What I Learned

During this project, I learned and implemented:

#   🧠 Core Concepts

What is RabbitMQ and why it is used
AMQP protocol basics (message routing rules)
Producers, Consumers, Queues, Exchanges
Message flow architecture

#   🔁 Messaging Patterns

1. Work Queues
Load balancing between multiple workers
Task distribution system
One message → one worker processing
2. Publish / Subscribe (Fanout Exchange)
Broadcasting messages to multiple consumers
One message → all consumers receive it
Used for notifications systems
3. Direct Exchange (Routing Key Based)
Exact matching using routing keys
Selective message delivery
Example: error logs, info logs
4. Topic Exchange (Pattern Matching ⭐)
Advanced routing using wildcards:
* → one word match

# → multiple words match

Example:
user.created
order.*
#.error

#   🔄 RPC (Remote Procedure Call)

Request-response model using RabbitMQ
Built using:
reply_to
correlation_id
Simulates function calls over network
Example: Fibonacci calculation service

#   📦 Queue Concepts

Message buffering system
Persistent vs non-persistent messages
Auto ACK vs Manual ACK
Message lifecycle in queue

#   ⚠️ DLQ (Dead Letter Queue Concept)

Storage for failed messages
Used when:
message processing fails
message expires (TTL)
message is rejected
Helps in debugging and reliability

#   🔧 Technologies Used

Python 🐍
RabbitMQ 🐇
AMQP Protocol
pika library
Docker (for running RabbitMQ server)
Linux environment

#   🏗️ Project Structure

RabbitMQ-hands-on/
│
├── send.py                # Basic producer
├── receive.py             # Basic consumer
├── new_task.py            # Work queue producer
├── worker.py              # Worker consumer
├── emit_log.py            # Fanout exchange example
├── receive_logs.py        # Fanout consumer
├── emit_log_direct.py     # Direct exchange producer
├── receive_logs_direct.py # Direct exchange consumer
├── emit_log_topic.py      # Topic exchange producer
├── receive_logs_topic.py  # Topic exchange consumer
├── rpc_client.py          # RPC client
├── rpc_server.py          # RPC server
└── README.md

#   ⚙️ Key Learning Flow

Producer → Exchange → Queue → Consumer
Advanced Flow (RPC)
Client → Queue → Worker → Response Queue → Client

#   🚀 Real-World Use Cases Learned

Background job processing (email, notifications)
Microservice communication
AI/ML pipeline task distribution
Logging systems
Event-driven architectures
Real-time processing systems

#   🧠 Key Insights

RabbitMQ is a task/message broker
AMQP defines messaging rules
Exchanges control routing logic
Queues store messages until processed
RPC can be built using queues + correlation IDs
Topic exchange is the most flexible routing system

#   🎯 What This Project Demonstrates

✔ Message-driven architecture
✔ Distributed system basics
✔ Async task processing
✔ Real-world backend system design
✔ Scalable microservice communication

#   📌 Author

Syed Usman Ali
AI Engineer | Backend Developer | FastAPI & Distributed Systems Learner