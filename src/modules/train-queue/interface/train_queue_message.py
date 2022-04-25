import json

class TrainQueueMessage:
    def __init__(self, input: object):
        self.model_name = input['model_name']
        self.branch_name = input['branch_name']
        self.email = input['email']

    def to_json(self) -> str:
        '''
            Serialize object to JSON string
        '''
        return json.dumps(self.__dict__)

    @staticmethod
    def validate(data: object) -> bool:
        '''
            TrainQueueMessage object validator method. Compares
            param obj to the structure of this class

            params:
                data: Any object
            returns:
                bool: True for valid; False otherwise
        '''
        # list of attributes input object must have
        atts = ['model_name', 'branch_name', 'email']   
        
        # try to access each field, return False on error
        try:
            for att in atts:
                _ = data[att]
            return True
        except:
            return False

    @staticmethod
    def get_structure():
        '''
            Error message string to describe the expected payload structure
        '''
        return "{ model_name: str, branch_name: str, email: str }"
