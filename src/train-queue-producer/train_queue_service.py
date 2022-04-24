class TrainQueueService:
    def ping(self):
        return "Train Queue API is Running"

    def process_train_queue_request(self, body):
        print(body)
