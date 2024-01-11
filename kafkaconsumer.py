# from confluent_kafka import Consumer, KafkaError

# # Kafka sunucu adresi ve konfigürasyon ayarları
# conf = {
#     'bootstrap.servers': '192.168.1.149:9092',
#     'group.id': '1',
#     'auto.offset.reset': 'latest', 
# }

# # Tüketiciyi oluştur
# consumer = Consumer(conf)

# # Tüketiciye abone olunacak konu
# topic = 'test'
# consumer.subscribe([topic])

# try:
#     while True:
#         # Mesajları tüket
#         msg = consumer.poll(1.0)

#         if msg is None:
#             print("BOS")
#             continue
#         if msg.error():
#             if msg.error().code() == KafkaError._PARTITION_EOF:
#                 # Eğer konu sona erdiyse devam et
#                 print("ee")
#                 continue
#             else:
#                 print(msg.error())
#                 break

#         # Gelen mesajları işle
#         print('Received message: {}'.format(msg.value().decode('utf-8')))

# except KeyboardInterrupt:
#     pass

# finally:
#     # Tüketiciyi kapat
#     consumer.close()


from confluent_kafka import Producer, Consumer
import time

# Kafka producer
producer_conf = {'bootstrap.servers': '192.168.1.149:9092'}
producer = Producer(producer_conf)

# Kafka consumer
consumer_conf = {
    'bootstrap.servers': '192.168.1.149:29092',
    'group.id': 'tester',
    'auto.offset.reset': 'latest'
}
consumer = Consumer(consumer_conf)
consumer.subscribe(['test'])

# Producing a message
producer.produce('test', value=b'Hello, Kafka!')
producer.flush()

# Consuming messages
while True:
    msg = consumer.poll(1.0)  # timeout in seconds
    if msg is None:
        print("NOMSG")
        continue
    if msg.error():
        print("Consumer error: {}".format(msg.error()))
        continue
    print("Received message: {}".format(msg.value().decode('utf-8')))
    time.sleep(1)  # Optional: slowing down the consumption for demonstration purposes
    print("BOS")