### Use Tumbling Windows to calculate the maximum temperature or parameter of your choice (any interval)

```commandline
docker-compose build 
docker-compose up -d 
docker-compose exec kafka kafka-topics.sh --bootstrap-server kafka:9092 --create --topic hw3 --partitions 3 --replication-factor 1
docker-compose exec kafka kafka-topics.sh --bootstrap-server kafka:9092 --create --topic hw3preprocessed --partitions 3 --replication-factor 1
docker-compose exec jobmanager ./bin/flink run -py /opt/pyflink/block2/tumbling_windows_job.py.py.py -d
python producer_1.py
python consumer_1.py
```

### Use Sliding Windows to calculate the maximum temperature or parameter of your choice (any interval)

```commandline
docker-compose build 
docker-compose up -d 
docker-compose exec kafka kafka-topics.sh --bootstrap-server kafka:9092 --create --topic hw3 --partitions 3 --replication-factor 1
docker-compose exec kafka kafka-topics.sh --bootstrap-server kafka:9092 --create --topic hw3preprocessed --partitions 3 --replication-factor 1
docker-compose exec jobmanager ./bin/flink run -py /opt/pyflink/block2/sliding_windows_job.py.py -d
python producer_1.py
python consumer_1.py
```

### Use Session Windows to calculate the maximum temperature or parameter of your choice (any interval)

```commandline
docker-compose build 
docker-compose up -d 
docker-compose exec kafka kafka-topics.sh --bootstrap-server kafka:9092 --create --topic hw3 --partitions 3 --replication-factor 1
docker-compose exec kafka kafka-topics.sh --bootstrap-server kafka:9092 --create --topic hw3preprocessed --partitions 3 --replication-factor 1
docker-compose exec jobmanager ./bin/flink run -py /opt/pyflink/block2/session_windows_job.py.py -d
python producer_1.py
python consumer_1.py
```