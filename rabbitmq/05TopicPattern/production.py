from rabbitconnection import connection

channel = connection.channel()

# 声明一个名为topic_logs 类型为topic的exchange
channel.exchange_declare(
    exchange='topic_logs',
    exchange_type='topic'
)

routing_keys = ['anonymous.info', 'kern.critical']
messages = ['Hello World!', 'A critical kernel error']

for i, key in enumerate(routing_keys):
    # 向名为topic_logs的exchange 按照设置的routing_key发送message
    channel.basic_publish(
        exchange='topic_logs',
        routing_key=key,
        body=messages[i].encode()
    )

    print(" [x] Sent %r:%r" % (key, messages[i]))
connection.close()
