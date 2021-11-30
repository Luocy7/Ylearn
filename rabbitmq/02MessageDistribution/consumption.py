import time
from rabbitconnection import connection

channel = connection.channel()
# 申明消息队列。当不确定生产者和消费者哪个先启动时，可以两边重复声明消息队列。
channel.queue_declare(queue='task_queue', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')


# 定义一个回调函数来处理消息队列中的消息，这里是打印出来
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body.decode())
    # 手动发送确认消息
    time.sleep(1)
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)


# 如果该消费者的channel上未确认的消息数达到了prefetch_count数，则不向该消费者发送消息
channel.basic_qos(prefetch_count=1)

channel.basic_consume(
    'task_queue',
    on_message_callback=callback,
    # auto_ack=True  # 自动发送确认消息
)

# 开始接收信息，并进入阻塞状态，队列里有信息才会调用callback进行处理
channel.start_consuming()
