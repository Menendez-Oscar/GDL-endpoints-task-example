# Sample App Engine: Cloud Endpoints
# Explained by Danny H, and Dan H from a GDL session
# This can be used as a starting point to create your own endpoints backend


from google.appengine.ext import endpoints
from google.appengine.ext import ndb
from endpoints_proto_datastore.ndb import EndpointsModel
from protorpc import remote


# Model
class Task(EndpointsModel):
    name = ndb.StringProperty(required=True)
    owner = ndb.StringProperty()


@endpoints.api(name="tasks", version="v1", description="api for tasks")
class TaskApi(remote.Service):
    # POST is the default http method, thus a declaration is not really needed.
    # The user_required field tell whether you want to require OAuth or not
    @Task.method(user_required=True,
                 name='task.insert', path='tasks', http_method='POST')
    def insert_tasks(self, request):
        Task(name=request.name, owner=request.owner).put()
        return request

    # GET is the default http method when using query_method, thus a declaration is not really needed.
    @Task.query_method(user_required=True,
                       query_fields=('limit', 'pageToken'),
                       name='task.list', path='tasks', http_method='GET')
    def list_tasks(self, query):
        return query


# create an application endpoints.api_server takes a list of APIs
application = endpoints.api_server([TaskApi])
