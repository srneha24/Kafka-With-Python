# KAFKA WITH PYTHON

## Tools And Technologies

- Python
- Kafka
- PostgresSQL

## Running The Project

1. Create the database table using the following SQL query -

   ```
   CREATE TABLE kafka_messages (
      id SERIAL,
      topic_name VARCHAR(50) NOT NULL,
      message VARCHAR(200) NOT NULL,
      created_at TIMESTAMP NOT NULL DEFAULT NOW(),
      PRIMARY KEY (id)
   );
   ```

2. Ensure Zookeeper and Kafka are running in the background.

   #### Running Zookeeper On Windows

   ```
   .\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties
   ```

   #### Running Kafka Server On Windows

   ```
   .\bin\windows\kafka-server-start.bat .\config\server.properties
   ```

3. Set up a .env file on project root with the following values -

   ```
   # KAFKA
   KAFKA_HOST=kafka-host
   KAFKA_PORT=kafka-port

   # DATABASE CONFIG
   DATABASE_NAME=database-name
   DATABASE_HOST=database-host
   DATABASE_PORT=database-port
   DATABASE_USER=database-user
   DATABASE_PASSWORD=database-password
   ```

4. Open a terminal and run `producer.py` using the following command -

   ```
   python producer.py
   ```

5. Open another terminal and run `consumer.py` using the followiing command -

   ```
   python consumer.py
   ```
