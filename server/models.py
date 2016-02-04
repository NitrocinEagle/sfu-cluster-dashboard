# -*- coding: utf-8 -*-
__author__ = 'mist'
from time import time
from mongoengine import *


class NodeInfo(Document):
    node_type = StringField(max_length=20)
    node_ip = StringField(max_length=15)
    node_name = StringField(max_length=50)
    node_os = StringField(max_length=30)
    enabled_plugins = ListField(StringField(max_length=50))


class ParamGeneralInfo(EmbeddedDocument):
    param_name = StringField(max_length=30)
    description = StringField(max_length=300)
    timeout = IntField(default=10)


class PluginInfo(Document):
    plugin_name = StringField(max_length=30)
    description = StringField(max_length=300)
    params_info = EmbeddedDocumentListField(ParamGeneralInfo)


class LineChartMetric(DynamicEmbeddedDocument):
    timestamp = IntField(default=int(time()))
    value = FloatField(default=0.0)


class PieChartMetric(DynamicEmbeddedDocument):
    class SectorData(EmbeddedDocument):
        sector_name = StringField(max_length=30)
        value = FloatField()

    timestamp = IntField(default=int(time()))
    data = EmbeddedDocumentListField(SectorData)


class ParamDescription(EmbeddedDocument):
    param_name = StringField(max_length=30)
    axis_y_title = StringField(max_length=20)
    axis_x_title = StringField(max_length=20, default="Time line")
    graph_type = StringField(max_length=30)


class NodeData(Document):
    node_name = StringField(max_length=50)
    node_ip = StringField(max_length=15)
    plugin_name = StringField(max_length=30)
    param_name = StringField(max_length=30)
    data = DynamicField(default=LineChartMetric)