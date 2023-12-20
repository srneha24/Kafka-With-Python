import os
import psycopg2
from kafka import KafkaConsumer
from json import loads
from dotenv import load_dotenv


class DBClient:
    conn = None

    def __init__(self) -> None:
        self.connect()

    def connect(self):
        load_dotenv()

        self.conn = psycopg2.connect(
            database=os.getenv('DATABASE_NAME'),
            host=os.getenv('DATABASE_HOST'),
            port=os.getenv('DATABASE_PORT'),
            user=os.getenv('DATABASE_USER'),
            password=os.getenv('DATABASE_PASSWORD')
        )

        print("DB Connection Successful")

    def insert(self, message, topic_name='testevent'):
        cursor = self.conn.cursor()
        query = "INSERT INTO kafka_messages (topic_name, message) VALUES (%s, %s);"
        cursor.execute(query, (topic_name, message))
        self.conn.commit()

        print("DB Insertion Successful")

    def close_connection(self):
        self.conn.close()


def deserialize(message):
    return loads(message.decode('utf-8'))


class KafkaConsumerClient:
    consumer: KafkaConsumer = None

    def __init__(self) -> None:
        self.consumer = KafkaConsumer(
            'testevent',
            bootstrap_servers=['localhost : 9092'],
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            value_deserializer=deserialize
        )


def main():
    try:
        consumer_client = KafkaConsumerClient()
        db_client = DBClient()

        for message in consumer_client.consumer:
            value = message.value
            db_client.insert(value)
    except KeyboardInterrupt:
        print("Closing DB Connection")
        db_client.close_connection()


if __name__ == "__main__":
    main()
