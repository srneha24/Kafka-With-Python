# KAFKA WITH PYTHON

## Tools And Technologies

- Python
- Kafka
- PostgresSQL

## Running The Project

1. Ensure Zookeeper and Kafka are running in the background.

   #### Running Zookeeper On Windows

   ```
   .\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties
   ```

   #### Running Kafka Server On Windows

   ```
   .\bin\windows\kafka-server-start.bat .\config\server.properties
   ```

2. Set up a .env file on project root with the following values -

   ```
   DATABASE_NAME=database-name
   DATABASE_HOST=database-host
   DATABASE_PORT=database-port
   DATABASE_USER=database-user
   DATABASE_PASSWORD=database-password
   ```

3. Open a terminal and run `producer.py` using the following command -

   ```
   python producer.py
   ```

4. Open another terminal and run `consumer.py` using the followiing command -

   ```
   python consumer.py
   ```
