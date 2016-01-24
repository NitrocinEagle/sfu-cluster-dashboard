__author__ = 'mist'
from mongoengine import Document, EmbeddedDocument, EmbeddedDocumentListField, \
    ListField, StringField, IntField


class NodeInfo(Document):
    node_type = StringField(max_length=20)
    node_ip = StringField(max_length=15)
    node_name = StringField(max_length=50)
    node_os = StringField(max_length=30)
    enabled_plugins = ListField(StringField(max_length=50),
                                default=["cpu_load", "ram_usage", "hdd_usage"])


class ParametresInfo(EmbeddedDocument):
    param_name = StringField(max_length=30)
    description = StringField(max_length=300)
    timeout = IntField(default=10)


class PluginInfo(Document):
    plugin_name = StringField(max_length=30)
    description = StringField(max_length=300)
    params_info = EmbeddedDocumentListField(ParametresInfo)
