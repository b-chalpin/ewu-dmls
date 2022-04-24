import cherrypy
from cherrypy.process.plugins import Daemonizer
from train_queue_controller import TrainQueueController

# mount the service
cherrypy.quickstart(TrainQueueController(), '/api/queue', "app.conf")

# # { '/api/queue': {
# #     'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
# #     'tools.trailing_slash.on': False
# #     }}
#     )

# # set config
# cherrypy.config.update("app.conf")

# # start the server
# cherrypy.engine.start()
# cherrypy.engine.block()
