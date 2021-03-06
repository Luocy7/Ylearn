import pika
from rabbitconnection import parameters


# Step #3
def on_open(connection):
    connection.channel(on_open_callback=on_channel_open)


# Step #4
def on_channel_open(channel):
    channel.basic_publish(
        exchange='',
        routing_key='hello',
        body='Hello world!'.encode('utf-8'),
        properties=pika.BasicProperties(
            content_type='text/plain',
            delivery_mode=1
        )
    )
    print(" [x] Sent 'Hello World!'")


connection = pika.SelectConnection(
    parameters=parameters,
    on_open_callback=on_open
)

try:

    # Step #2 - Block on the IOLoop
    connection.ioloop.start()

# Catch a Keyboard Interrupt to make sure that the connection is closed cleanly
except KeyboardInterrupt:

    # Gracefully close the connection
    connection.close()

    # Start the IOLoop again so Pika can communicate, it will stop on its own when the connection is closed
    connection.ioloop.start()
