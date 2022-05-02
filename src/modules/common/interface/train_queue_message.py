import json

class TrainQueueMessage:
    def __init__(self, input: object):
        self.model_name = input['model_name']
        self.branch_name = input['branch_name']
        self.email = input['email']

    def to_json(self) -> str:
        '''
            Serialize object to JSON string.
            
            returns:
                str: JSON string representation of this object
        '''
        return json.dumps(self.__dict__)

    @staticmethod
    def validate(data: object) -> bool:
        '''
            TrainQueueMessage object validator method. Compares
            param obj to the structure of this class.

            params:
                data: Any object
            returns:
                bool: True for valid; False otherwise
        '''
        required_atts = ['model_name', 'branch_name', 'email']   
        try:
            for att in required_atts:
                _ = data[att]
            return True
        except:
            return False

    @staticmethod
    def get_json_structure() -> str:
        """
        Return a string representation of the required JSON structure of this class. 
        Used in 400 error messages.

        returns:
            str: target JSON structure
        """
        return "{ model_name: str, branch_name: str, email: str }"
