from google.appengine.ext import ndb


class Question(ndb.Model):
    question = ndb.StringProperty()
    one = ndb.StringProperty()
    two = ndb.StringProperty()
    three = ndb.StringProperty()
    four = ndb.StringProperty()
    category = ndb.StringProperty()
    correct	= ndb.StringProperty()
    difficulty = ndb.IntegerProperty()