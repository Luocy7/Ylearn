from rabbitconnection import connection

channel = connection.channel()
# 申明消息队列。当不确定生产者和消费者哪个先启动时，可以两边重复声明消息队列。
channel.queue_declare(queue='hello', durable=False)


# 定义一个回调函数来处理消息队列中的消息，这里是打印出来
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body.decode())
    # 手动发送确认消息 消费者消费完毕后手动地向 Broker 发送确认通知，Broker 收到确认通知后再从队列中删除对应的消息
    ch.basic_ack(delivery_tag=method.delivery_tag)


def on_message(ch, method_frame, header_frame, body):
    print(method_frame.delivery_tag)
    print(" [x] Received %r" % body.decode())
    # 手动发送确认消息 消费者消费完毕后手动地向 Broker 发送确认通知，Broker 收到确认通知后再从队列中删除对应的消息
    ch.basic_ack(delivery_tag=method_frame.delivery_tag)


channel.basic_consume(
    queue='hello',
    on_message_callback=on_message,
    # auto_ack=True  # 自动发送确认消息 Broker（RabbitMQ 服务器）在将消息发送给消费者后即将消息从队列中删除，
    # 无论消费者是否消费成功。如果消费者消费时业务代码出现异常或者还未消费完毕时系统宕机，就会导致消息丢失
)

print(' [*] Waiting for messages. To exit press CTRL+C')
# 开始接收信息，并进入阻塞状态，队列里有信息才会调用callback进行处理
try:
    channel.start_consuming()
except KeyboardInterrupt:
    channel.stop_consuming()
connection.close()
