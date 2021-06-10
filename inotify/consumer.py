import pulsar

client = pulsar.Client('pulsar://localhost:6650')
consumer = client.subscribe('my-topic', 'my-subscription')

while True:
     msg = consumer.receive()
     try:
        print("received message '{}' id='{}'".format(msg.data(),msg.message_id()))
        consumer.acknowledge(msg)
     except:
        consumer.negative-acknowledge(msg)

client.close()
