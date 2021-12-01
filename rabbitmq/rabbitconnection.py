import pika

USERNAME = "admin"
PASSWORD = "Hs12#"

credentials = pika.PlainCredentials(USERNAME, PASSWORD)  # mq用户名和密码，没有则需要自己创建

parameters = pika.ConnectionParameters(
    host='192.168.110.32',
    port=5672,
    virtual_host='/',
    credentials=credentials
)

# 虚拟队列需要指定参数 virtual_host，如果是默认的可以不填。
connection: pika.BlockingConnection = pika.BlockingConnection(parameters=parameters)
