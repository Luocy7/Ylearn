from rabbitconnection import connection

channel = connection.channel()

# 作为好的习惯，在producer和consumer中分别声明一次以保证所要使用的exchange存在
channel.exchange_declare(
    exchange='logs',
    exchange_type='fanout'
)

# 随机生成一个新的空的queue，将exclusive置为True，这样在consumer从RabbitMQ断开后会删除该queue
# 是排他的。
result = channel.queue_declare('', exclusive=True)

# 用于获取临时queue的name
queue_name = result.method.queue

# exchange与queue之间的关系成为binding
# binding告诉exchange将message发送该哪些queue
channel.queue_bind(
    exchange='logs',
    queue=queue_name
)


# 定义一个回调函数来处理消息队列中的消息，这里是打印出来
def callback(ch, method, properties, body):
    # 手动发送确认消息
    print(body.decode())
    # 告诉生产者，消费者已收到消息
    # ch.basic_ack(delivery_tag=method.delivery_tag)


# 如果该消费者的channel上未确认的消息数达到了prefetch_count数，则不向该消费者发送消息
channel.basic_qos(prefetch_count=1)
# 告诉rabbitmq，用callback来接收消息
# 默认情况下是要对消息进行确认的，以防止消息丢失。
# 此处将no_ack明确指明为True，不对消息进行确认。
channel.basic_consume(
    queue=queue_name,
    on_message_callback=callback,
    # auto_ack=True  # 自动发送确认消息
)
# 开始接收信息，并进入阻塞状态，队列里有信息才会调用callback进行处理
channel.start_consuming()
