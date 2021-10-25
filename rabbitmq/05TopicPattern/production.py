from rabbitconnection import connection

channel = connection.channel()

# 声明一个名为topic_logs 类型为topic的exchange
channel.exchange_declare(
    exchange='topic_logs',
    exchange_type='topic'
)

severity = '*.rabbit.*'
message = 'Hello World!'

# 向名为topic_logs的exchange 按照设置的routing_key发送message
channel.basic_publish(
    exchange='topic_logs',
    routing_key=severity,
    body=message.encode()
)

print(" [x] Sent %r:%r" % (severity, message))
connection.close()
