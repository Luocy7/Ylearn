from rabbitconnection import connection

channel = connection.channel()

# 声明一个名为direct_logs 类型为direct的exchange
channel.exchange_declare(
    exchange='direct_logs',
    exchange_type='direct'
)

severity = 'info'
message = 'Hello World!'

# 向名为direct_logs的exchage 按照设置的routing_key发送message
channel.basic_publish(
    exchange='direct_logs',
    routing_key=severity,
    body=message.encode()
)

print(" [x] Sent %r:%r" % (severity, message))
connection.close()
