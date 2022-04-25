class TrainQueueService:
    def ping(self) -> str:
        return "Train Queue API is Running"

    def process_train_queue_request(self, body) -> None:
        print(f"PROCESS STUFF HERE: {body}")
