__author__ = 'Kirill Korovin'

from endpoints_proto_datastore.ndb import EndpointsModel
from google.appengine.ext import ndb


class Item(EndpointsModel):

    _message_fields_schema = ()