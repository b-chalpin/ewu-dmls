import cherrypy
from train_queue_service import TrainQueueService
from interface.train_queue_message import TrainQueueMessage

@cherrypy.expose
class TrainQueueApi(object):
    service = TrainQueueService()
    
    def GET(self):
        '''
            Default GET API. Returns status that application is running
        '''
        return self.service.ping()
    
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def POST(self):
        '''
            Default POST API to receive train message. Validates 
            and pushes the message into the train queue
            
            returns:
                { success: bool }; returns True if success; else error message
        '''
        try:
            body = cherrypy.request.json
        except:
            raise cherrypy.HTTPError(400, 'Body must not be empty.')

        if not TrainQueueMessage.validate(body):
            raise cherrypy.HTTPError(400, f'Invalid payload. Body must have structure {TrainQueueMessage.get_structure()}')

        train_message = TrainQueueMessage(body)
        
        cherrypy.log(train_message.to_json())

        self.service.process_train_queue_request(train_message)

        return { "success": True }

if __name__ == "__main__": 
    cherrypy.quickstart(TrainQueueApi(), '/api/queue', 'C:/git/school/ewu-dmls/src/modules/train-queue/train_queue_app.conf')
