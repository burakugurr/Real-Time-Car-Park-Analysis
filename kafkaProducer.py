from confluent_kafka import Producer
import socket

conf = {'bootstrap.servers': '192.168.1.149:9092',
        'client.id': socket.gethostname()}

print(socket.gethostname())

producer = Producer(conf)

def acked(err, msg):
    if err is not None:
        print("Failed to deliver message: %s: %s" % (str(msg), str(err)))
    else:
        print("Message produced: %s" % (str(msg)))

producer.produce("test", key="key", value="value", callback=acked)


producer.flush()