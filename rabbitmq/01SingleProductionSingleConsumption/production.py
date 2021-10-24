from rabbitconnection import connection

# 建立rabbit协议的通道
channel = connection.channel()
# 声明消息队列，消息将在这个队列传递，如不存在，则创建。durable指定队列是否持久化
channel.queue_declare(queue='python-test', durable=False)

# message不能直接发送给queue，需经exchange到达queue，此处使用以空字符串标识的默认的exchange
# 向队列插入数值 routing_key是队列名
channel.basic_publish(
    exchange='',
    routing_key='python-test',
    body='Hello world!'.encode('utf-8')
)
# 关闭与rabbitmq server的连接
connection.close()
