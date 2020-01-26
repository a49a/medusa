from kafka import KafkaProducer


producer = KafkaProducer(bootstrap_servers='127.0.0.1:9092')
for _ in range(10):
    producer.send('foo-topic', b"hahaha")

producer.flush()
producer.close()

