__author__ = 'mist'
from dashboard.app.dashboard.models import NodeInfo

from mongoengine import connect
connect('test')

node = NodeInfo.objects().first()
print node