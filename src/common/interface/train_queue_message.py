import json

class TrainQueueMessage:
    def init(self, model_name: str, branch_name: str, email: str):
        self.model_name = model_name
        self.branch_name = branch_name
        self.email = email

    def to_json(self) -> str:
        return json.dumps({ self.model_name, self.branch_name, self.email })

    @staticmethod
    def validate(other) -> bool:
        '''
            TrainQueueMessage object validator method. Compares
            param obj to the structure of this class

            params:
                other: Any
            returns:
                bool: True for valid; False otherwise
        '''
        return True

    @staticmethod
    def get_structure():
        '''
            Error message string to describe the expected payload structure
        '''
        return "{ model_name: str, branch_name: str,  email: str }"
