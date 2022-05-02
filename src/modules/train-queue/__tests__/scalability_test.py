import requests
import json

NUM_REQUESTS = 10
TRAIN_QUEUE_API = "http://127.0.0.1:7999/api/queue"
TRAIN_QUEUE_API_PORT = 7999

PAYLOAD_EMAIL = "bchalpin@ewu.edu"
PAYLOAD_BRANCH_NAME = "main"

# random generate the model name
for i in range(NUM_REQUESTS):
    payload = { "model_name": f"model-{i}",
                "branch_name": PAYLOAD_BRANCH_NAME,
                "email": PAYLOAD_EMAIL }

    headers = { "Content-type": "application/json" }
    
    r = requests.post(url=TRAIN_QUEUE_API, headers=headers, data=json.dumps(payload))
    
    print(f"({i}) Response: {r.text}")
