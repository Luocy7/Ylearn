import pika

USERNAME = "admin"
PASSWORD = "admin"

credentials = pika.PlainCredentials(USERNAME, PASSWORD)  # mq用户名和密码，没有则需要自己创建
# 虚拟队列需要指定参数 virtual_host，如果是默认的可以不填。
connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host='localhost',
        port=5672,
        virtual_host='/',
        credentials=credentials
    )
)
