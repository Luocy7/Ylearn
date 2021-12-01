import pika.exceptions
from rabbitconnection import connection

# 建立rabbit协议的通道
channel = connection.channel()
# 声明消息队列，消息将在这个队列传递，如不存在，则创建. durable指定队列是否持久化
channel.queue_declare(queue='hello')

# Enabled delivery confirmations. This is REQUIRED.
channel.confirm_delivery()
# message不能直接发送给queue，需经exchange到达queue，此处使用以空字符串标识的默认的exchange
# 向队列插入数值 routing_key是队列名

try:
    channel.basic_publish(
        exchange='',
        routing_key='hello1',
        body='Hello world!'.encode('utf-8'),
        properties=pika.BasicProperties(content_type='text/plain',
                                        delivery_mode=1),
        mandatory=True  # mandatory会设置消息投递失败的策略，有两种策略：true是返回客户端，false是自动删除
    )
    print(" [x] Sent 'Hello World!'")
except pika.exceptions.UnroutableError:
    print('Message was returned')
# 关闭与rabbitmq server的连接
connection.close()
