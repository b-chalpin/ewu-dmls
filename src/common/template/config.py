def generate_model_config():

    # change the values below
    config = {
        "epochs": 10,
        "batch_size": 24,
        "optimizer": "rmsprop",
        "loss": "categorical_crossentropy",
        "metrics": ["accuracy"]
    }

    return config
