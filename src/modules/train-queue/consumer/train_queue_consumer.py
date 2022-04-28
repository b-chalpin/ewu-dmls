import sys
sys.path.append("../..")

import pika, os
from common.utils.evironment_utils import load_env

def main():
    queue_name = os.environ.get("RABBIT_TRAIN_QUEUE")
    rabbit_host = os.environ.get("RABBIT_HOST")
    
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbit_host))
    channel = connection.channel()

    channel.queue_declare(queue=queue_name)

    def callback(ch, method, properties, body):
        print(f"Consuming message: {body}")

    channel.basic_consume(queue=queue_name, 
                          on_message_callback=callback, 
                          auto_ack=True)

    print("Consumer is running. Waiting for messages...")
    channel.start_consuming()

if __name__ == '__main__':
    load_env("../.env") # load our environment vars
    main()
    