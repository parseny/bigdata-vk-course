import random
import time
import functools

from kafka import KafkaConsumer


class ServiceException(Exception):
    pass


def backoff(tries, sleep):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < tries:
                try:
                    print(f'Backoff attempt {attempts}: trying to call {func.__name__}')
                    return func(*args, **kwargs)
                except ServiceException as e:
                    attempts += 1
                    print(f"Backoff attempt {attempts}/{tries} failed: {e}")
                    if attempts < tries:
                        time.sleep(sleep)
                    else:
                        break
            print('Backoff finished\n')

        return wrapper

    return decorator


@backoff(tries=3, sleep=1)
def message_handler(value) -> bool:
    rand_num = random.randint(0, 10)
    if rand_num % 2 == 0:
        print(value)
    else:
        raise ServiceException("Random number condition not met")


def create_consumer():
    print("Connecting to Kafka brokers")
    consumer = KafkaConsumer("hw3",
                             group_id='hw3-group1',
                             bootstrap_servers='localhost:29092',
                             auto_offset_reset='earliest',
                             enable_auto_commit=True)

    for message in consumer:
        # send to http get (rest api) to get response
        # save to db message (kafka) + external
        message_handler(message)
        print(message)


if __name__ == '__main__':
    create_consumer()
