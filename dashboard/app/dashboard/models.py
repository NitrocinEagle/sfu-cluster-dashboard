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


class ParamData(EmbeddedDocument):
    param_description = EmbeddedDocumentField(ParamDescription)
    dataset = DynamicField(default=LineChartMetric)


class PluginData(EmbeddedDocument):
    plugin_name = StringField(max_length=30)
    param_data_list = EmbeddedDocumentListField(ParamData)


class NodeData(Document):
    node_name = StringField(max_length=50)
    node_ip = StringField(max_length=15)
    plugin_data_list = EmbeddedDocumentListField(PluginData)


"""
Описание формата собранных данных для конкретного узла. Собранные даные разбиты на фрагменты по плагинам.
В каждом фрагменте содержится:
1. Название плагина;
2. Параметры.

В параметрах в зависимости от способа отображения могут хранится:
1. Название параметра;
2. Метка для оси X;
3. Метка для оси Y;
4. Способ отображения данного параметра;
5. Набор данных, который нужно отображать.

В наборе данных содержатся данные в формате, требуемом от способа отображения.
"""

"""
Здесь хранятся данные мониторинга для каждого узла. В каждом наборе данных определены:
1. Имя узла;
2. Ip-адрес узла;
3. Собранные данные. (формат собранных данных описан выше)
"""
