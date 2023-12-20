import os
import time
from kafka import KafkaProducer
from json import dumps
from dotenv import load_dotenv


load_dotenv()


def serializer(message):
    return dumps(message).encode('utf-8')


class KafkaProducerClient:
    producer: KafkaProducer = None

    def __init__(self) -> None:
        self.producer = KafkaProducer(
            bootstrap_servers=[
                f"{os.getenv('KAFKA_HOST')}:{os.getenv('KAFKA_PORT')}"],
            value_serializer=serializer
        )

    def produce_event(self, topic_name, message):
        result = self.producer.send(
            topic=topic_name,
            value=message
        )

        print(result.get())


def main():
    producer_client = KafkaProducerClient()

    for i in range(5):
        producer_client.produce_event("testevent", str(i))
        time.sleep(10)


if __name__ == "__main__":
    main()
