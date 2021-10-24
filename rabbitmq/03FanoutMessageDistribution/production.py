from rabbitconnection import connection

# 建立rabbit协议的通道
channel = connection.channel()
# fanout: 所有绑定到此exchange的queue都可以接收消息（实时广播）
# direct: 通过routingKey和exchange决定的那一组的queue可以接收消息（有选择接受）
# topic： 所有符合routingKey(此时可以是一个表达式)的routingKey所bind的queue可以接收消息（更细致的过滤）
channel.exchange_declare('logs', exchange_type='fanout')

# 因为是fanout广播类型的exchange，这里无需指定routing_key
for i in range(10):
    channel.basic_publish(exchange='logs',
                          routing_key='',
                          body='Hello world！%s' % i)

# 关闭与rabbitmq server的连接
connection.close()
