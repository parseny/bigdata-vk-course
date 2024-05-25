# Practice tasks with Kafka and Flink


**Deploy Flink + Kafka Locally via Docker-Compose:**
   - Seting up a local environment using Docker-Compose to run both Flink and Kafka.


```commandline
docker-compose build
```


```commandline
docker-compose up -d
```

```commandline
docker-compose ps
```
```
http://localhost:8081/#/overview

```
```commandline
docker-compose down -v
```

```commandline
docker-compose exec kafka kafka-topics.sh --bootstrap-server kafka:9092 --create --topic topic_name --partitions 1 --replication-factor 1
```
```commandline
docker-compose exec kafka kafka-topics.sh --bootstrap-server kafka:9092 --describe itmo  
```
```commandline
 docker-compose exec kafka kafka-topics.sh --bootstrap-server kafka:9092 --alter --topic itmo --partitions 2

```

```commandline
docker-compose exec jobmanager ./bin/flink run -py /opt/pyflink/device_job.py -d  
```


### Block 1 (Flink checkpoint)

1. **Create a Kafka Source and Consumer:**
   - Develop a Kafka message source and consumer.

2. **Configure Flink Checkpointing and Save to Local Directory:**
   - Set up Flink checkpointing to save checkpoints in a local directory: `file:///opt/pyflink/tmp/checkpoints/logs`.
   - Ensure the recovery mechanism is in place.

3. **Configure Flink Checkpointing and Save to HDFS:**
   - Set up HDFS using Docker-Compose.
   - Configure Flink checkpointing to save checkpoints in HDFS.


### Block 2 (Flink Window)

1. **Create a Kafka Source and Consumer:**
   - Develop a Kafka message source and consumer (refer to seminar example).

2. **Tumbling Windows:**
   - Use Tumbling Windows to calculate the maximum temperature or another parameter of your choice (any interval).

3. **Sliding Windows:**
   - Use Sliding Windows to calculate the maximum temperature or another parameter of your choice (any interval).

4. **Session Windows:**
   - Use Session Windows to calculate the maximum temperature or another parameter of your choice (any interval).

### Block 3 (Kafka Backoff)

1. **Create a Kafka Source and Consumer:**
   - Develop a Kafka message source and consumer (refer to seminar example).

2. **Write a Custom Backoff Mechanism for Kafka Consumer using a Decorator (25 points):**
   - Implement a backoff mechanism for the Kafka consumer using a decorator as shown below:

```python
@backoff(tries=10, sleep=60)
def message_handler(value) -> None:
    print(value)
```