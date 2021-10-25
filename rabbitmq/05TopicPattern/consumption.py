from rabbitconnection import connection

channel = connection.channel()

# 声明一个名为topic_logs 类型为topic的exchange
# 同时在producer和consumer中声明exchage或queue是个好习惯，以保证其存在
channel.exchange_declare(
    exchange='topic_logs',
    exchange_type='topic'
)

result = channel.queue_declare('', exclusive=True)
queue_name = result.method.queue

# binding_keys = ["kern.*", "*.critical"]
binding_keys = ["#"]  # receive all the logs

for binding_key in binding_keys:
    # exchange和queue之间的binding可接受routing_key参数
    # fanout类型的exchange直接忽略该参数。direct类型的exchange精确匹配该关键字进行message路由
    # 一个消费者可以绑定多个routing_key
    # Exchange就是根据这个RoutingKey和当前Exchange所有绑定的BindingKey做匹配，
    # 如果满足要求，就往BindingKey所绑定的Queue发送消息
    channel.queue_bind(
        exchange='topic_logs',
        queue=queue_name,
        routing_key=binding_key
    )


def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body.decode(),))


print(' [*] Waiting for logs. To exit press CTRL+C')

channel.basic_consume(
    queue=queue_name,
    on_message_callback=callback,
    auto_ack=True
)

channel.start_consuming()
