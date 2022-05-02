import pika
import os
import cherrypy
import sys
sys.path.append("../..")

from common.interface.train_queue_message import TrainQueueMessage

class TrainQueueService:
    def ping(self) -> str:
        return "Train Queue API is Running"

    def process_train_queue_request(self, body: TrainQueueMessage) -> None:
        payload = body.to_json()
        
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=os.environ.get("RABBIT_HOST")))
        channel = connection.channel()

        channel.queue_declare(queue=os.environ.get("RABBIT_TRAIN_QUEUE"))

        channel.basic_publish(exchange=os.environ.get("RABBIT_TRAIN_DIRECT_EXCHANGE"), 
                              routing_key=os.environ.get("RABBIT_TRAIN_QUEUE_ROUTING_KEY"), 
                              body=payload)
        
        cherrypy.log(f"Published {payload} message")
        connection.close()
