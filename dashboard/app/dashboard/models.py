__author__ = 'mist'
from mongoengine import Document, ListField, StringField

class NodeInfo(Document):
    node_type = StringField(max_length=20)
    node_name = StringField(max_length=50)
    node_os = StringField(max_length=30)
    enabled_plugins = ListField(StringField(max_length=50), default=["cpu_load", "ram_usage", "hdd_usage"])