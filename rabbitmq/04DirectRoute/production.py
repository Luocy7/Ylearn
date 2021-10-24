# 生产者代码，测试命令可以使用：python produce.py error 404error
import sys
from rabbitconnection import connection

channel = connection.channel()

# 声明一个名为direct_logs的direct类型的exchange
# direct类型的exchange
channel.exchange_declare(exchange='direct_logs',
                         exchange_type='direct')

# 从命令行获取basic_publish的配置参数
severity = sys.argv[1] if len(sys.argv) > 1 else 'info'
message = ' '.join(sys.argv[2:]) or 'Hello World!'

# 向名为direct_logs的exchage按照设置的routing_key发送message
channel.basic_publish(exchange='direct_logs',
                      routing_key=severity,
                      body=message)

print(" [x] Sent %r:%r" % (severity, message))
connection.close()
