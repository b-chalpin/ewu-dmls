import sys
sys.path.append('../common/interface')

import json
import cherrypy
from train_queue_service import TrainQueueService
from train_queue_message import TrainQueueMessage

class TrainQueueController(object):
    service = TrainQueueService()

    @cherrypy.expose
    def ping(self):
        '''
            Health check API

            returns:
                string if application is running
        '''
        return self.service.ping()

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def index(self):
        '''
            Receives user request to train a model

            body:
                model_name: string representing the folder name of the model
                branch_name: git branch where the model is pushed
                email: email to be subscribed to the train process
        '''
        # why is cherrypy not seeing this is a POST method?
        # if cherrypy.request.method != 'POST':
        #     raise cherrypy.HTTPError(404, f'{cherrypy.request.method} /api/queue not found. Please use the POST method')

        try:
            body = cherrypy.request.body
        except:
            raise cherrypy.HTTPError(400, 'Body must not be empty.')

        cherrypy.log(f"BODY: {body}")

        if not TrainQueueMessage.validate(body):
            raise cherrypy.HTTPError(400, f'Invalid payload. Body must have structure {TrainQueueMessage.get_structure()}')

        train_message = TrainQueueMessage(body.model_name, body.branch_name, body.email)

        self.service.process_train_queue_request(train_message)

        return { "success": True }
