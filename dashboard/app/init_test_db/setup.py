# -*- coding: utf-8 -*-
# from setups_test_data import (save_nodes_info,
#                               save_node_groups, save_plugins_info,
#                               # save_previews_constructor, save_nodes_data,
#                               save_params_info)
# from test_data import *
#
# # save_nodes_data(nodes_data)
# save_nodes_info(nodes_info)
# save_params_info(params_info)
# save_plugins_info(plugins_info)
# # save_previews_constructor(previews_constructor)
# save_node_groups(NODE_GROUPS)
#
#
#
#
#
# __author__ = 'mist'
# from dashboard.app.mongo_models import LineChartMetric, PieChartMetric

PRINT = False
from time import time
from mongoengine import *

lengths = {
    'group_name': 30,
    'plugin': 30,
    'param': 30,
    'os': 30,
    'node_type': 20,
    'node_name': 50,
    'ip': 15,
    'description': 300
}


class MonitoringInfo(Document):
    node = StringField(max_length=lengths['node_name'])
    ip = StringField(max_length=lengths['ip'])
    plugin = StringField(max_length=lengths['plugin'])
    param = StringField(max_length=lengths['param'])
    timeout = IntField(min_value=0, default=0)


class NodeGroups(Document):
    name = StringField(max_length=lengths['group_name'])
    enabled_nodes = ListField(StringField(max_length=lengths['node_name']))


class ServerInfoDict(EmbeddedDocument):
    name = StringField()
    value = StringField()
    fa_icon = StringField()
    label = StringField()


class ServerInfo(Document):
    info = EmbeddedDocumentListField(ServerInfoDict)


class NodeInfo(Document):
    node_ip = StringField(max_length=lengths['ip'])
    node_name = StringField(max_length=lengths['node_name'])
    node_os = StringField(max_length=lengths['os'])
    enabled_plugins = ListField(StringField(max_length=lengths['plugin']))


class ParamInfo(Document):
    plugin_name = StringField(max_length=lengths['plugin'])
    param_name = StringField(max_length=lengths['param'])
    description = StringField(max_length=lengths['description'])
    axis_y_title = StringField(max_length=20, default=param_name)
    axis_x_title = StringField(max_length=20, default="Time line")
    graph_type = StringField(max_length=30)
    timeout = IntField(default=10)


class PluginInfo(Document):
    plugin_name = StringField(max_length=lengths['plugin'])
    description = StringField(max_length=lengths['description'])


class LineChartMetric(DynamicEmbeddedDocument):
    timestamp = IntField(default=int(time()))
    value = FloatField(default=0.0)


class PieChartMetric(DynamicEmbeddedDocument):
    class SectorData(EmbeddedDocument):
        sector_name = StringField(max_length=30)
        value = FloatField()

    timestamp = IntField(default=int(time()))
    data = EmbeddedDocumentListField(SectorData)


class NodeData(Document):
    node_name = StringField(max_length=lengths['node_name'])
    node_ip = StringField(max_length=lengths['ip'])
    plugin_name = StringField(max_length=lengths['plugin'])
    param_name = StringField(max_length=lengths['param'])
    data = DynamicField(default=LineChartMetric)


class PreviewCostructor(Document):
    username = StringField(max_length=255)
    node_name = StringField(max_length=lengths['node_name'])
    node_ip = StringField(max_length=lengths['ip'])
    plugin_name = StringField(max_length=lengths['plugin'])
    param_name = StringField(max_length=lengths['param'])


class MonitoringNodesData(Document):
    node = StringField(max_length=lengths['node_name'])
    plugin = StringField(max_length=lengths['plugin'])
    param = StringField(max_length=lengths['param'])
    data = DynamicField()
    timestamp = DateTimeField()

def get_dataset(graph_type, metric):
    dataset = []
    if graph_type is 'line_chart':
        for data_point in metric:
            if PRINT:
                print 'new_point: '
            new_point = LineChartMetric(
                timestamp=data_point['timestamp'],
                value=data_point['value']
            )
            if PRINT:
                print '\ttimestamp: ', new_point.timestamp
                print '\tvalue: ', new_point.value
            dataset.append(new_point)
        return dataset
    if graph_type is 'pie_chart':
        for sector in metric:
            if PRINT:
                print 'sector: ', sector
            new_sector = PieChartMetric()
            new_sector.timestamp = sector['timestamp']
            new_sector.data = []
            if PRINT:
                print 'new_sector: '
                print '\ttimestamp: ', new_sector.timestamp
                print '\tsector_data: '
            for sector_data in sector['data']:
                new_sector_data = new_sector.SectorData(
                    sector_name=sector_data['sector_name'],
                    value=round(sector_data['value'], 2)
                )
                if PRINT:
                    print '\t\tname: ', new_sector_data.sector_name
                    print '\t\tvalue: ', new_sector_data.value
                new_sector.data.append(new_sector_data)
            dataset.append(new_sector)
        return dataset
    return None


from mongoengine import connect

connect("test_monitoring")


def save_plugins_info(plugins_info):
    for plugin in plugins_info:
        new_plugin = PluginInfo()
        new_plugin.plugin_name = plugin['plugin_name']
        new_plugin.description = plugin['description']

        if not PluginInfo.objects(plugin_name=plugin['plugin_name']).first():
            new_plugin.save()

        if PRINT:
            plugins = PluginInfo.objects()
            print plugins[0].params_info[0].description


def save_nodes_info(nodes_info):
    for node in nodes_info:
        new_node = NodeInfo(
            node_ip=node['node_ip'],
            node_name=node['node_name'],
            node_os=node['node_os'],
            enabled_plugins=node['enabled_plugins']
        )
        if not NodeInfo.objects(node_name=node['node_name']).first():
            new_node.save()

        if PRINT:
            nodes = NodeInfo.objects()
            for node in nodes:
                print 'Node ', node.node_name
                print '\tnode_type is ', node.node_type
                print '\tnode_ip is ', node.node_ip
                print '\tnode_os is ', node.node_os
                print '\tenabled_plugins: ', node.enabled_plugins


def save_params_info(params_info):
    for param in params_info:
        new_param = ParamInfo(
            plugin_name=param['plugin_name'],
            param_name=param['param_name'],
            description=param['description'],
            axis_y_title=param['axis_y_title'],
            axis_x_title=param['axis_x_title'],
            graph_type=param['graph_type'],
            timeout=param['timeout'],
        )
        if not ParamInfo.objects(
                param_name=param['param_name'],
                plugin_name=param['plugin_name']).first():
            new_param.save()

def save_node_groups(groups):
    for group in groups:
        new_group = NodeGroups(name=group['name'],
                               enabled_nodes=group['enabled_nodes'])
        if not NodeGroups.objects(name=group['name']):
            new_group.save()


def save_monitoring_info(monitoring_info):
    for info in monitoring_info:
        new_info = MonitoringInfo(node=info['node'], ip=info['ip'],
                                  plugin=info['plugin'], param=info['param'],
                                  timeout=info['timeout'])
        if not MonitoringInfo.objects(node=info['node'], ip=info['ip'],
                                      plugin=info['plugin'], param=info['param'],
                                      timeout=info['timeout']):
            new_info.save()






PLUGINS = ("CPU", "RAM", "HDD")

MONITORING_INFO = [
    {
        "node": 'ULK416-cluster1-0',
        "ip": "127.0.0.1",
        "plugin": "CPU",
        "param": "cpu_percent",
        "timeout": 1,
    },
    {
        "node": 'ULK416-cluster1-0',
        "ip": "127.0.0.1",
        "plugin": "RAM",
        "param": "virtual_memory",
        "timeout": 2,
    },
    {
        "node": 'ULK416-cluster1-0',
        "ip": "127.0.0.1",
        "plugin": "HDD_USAGE_PLUGIN",
        "param": "disk_usage",
        "timeout": 3600,
    },
    {
        "node": 'ULK416-cluster1-1',
        "ip": "192.168.0.1",
        "plugin": "CPU",
        "param": "cpu_percent",
        "timeout": 2,
    },
    {
        "node": 'ULK416-cluster1-1',
        "ip": "192.168.0.1",
        "plugin": "RAM",
        "param": "virtual_memory",
        "timeout": 3,
    },
    {
        "node": 'ULK416-cluster1-1',
        "ip": "192.168.0.1",
        "plugin": "HDD_USAGE_PLUGIN",
        "param": "disk_usage",
        "timeout": 10000,
    },
    {
        "node": 'ULK416-cluster1-2',
        "ip": "192.168.0.2",
        "plugin": "CPU",
        "param": "cpu_percent",
        "timeout": 1,
    },
    {
        "node": 'ULK416-cluster1-2',
        "ip": "192.168.0.2",
        "plugin": "RAM",
        "param": "virtual_memory",
        "timeout": 5,
    },
    {
        "node": 'ULK416-cluster1-2',
        "ip": "192.168.0.2",
        "plugin": "HDD_USAGE_PLUGIN",
        "param": "disk_usage",
        "timeout": 7200,
    },
]

NODE_GROUPS = [
    {
        'name': 'group_1',
        'enabled_nodes': ['ULK416-cluster1-0', 'ULK416-cluster1-1']
    },
    {
        'name': 'group_2',
        'enabled_nodes': ['ULK416-cluster1-1', 'ULK416-cluster1-2']
    }
]
NODES = [
    {
        "name": "ULK416-cluster1-0",
        "ip": "127.0.0.1"
    },
    {
        "name": "ULK416-cluster1-1",
        "ip": "192.168.0.1"
    },
    {
        "name": "ULK416-cluster1-2",
        "ip": "192.168.0.2"
    },
]
GRAPHS = ("line_chart", "stacked_area", "pie_chart",)

nodes_info = [
    {
        "node_name": NODES[0]['name'],
        "node_ip": NODES[0]['ip'],
        "node_os": "Red Hat Linux",
        "enabled_plugins": PLUGINS,
    },
    {
        "node_name": NODES[1]['name'],
        "node_ip": NODES[1]['ip'],
        "node_os": "CentOS",
        "enabled_plugins": PLUGINS,
    },
    {
        "node_ip": NODES[2]['ip'],
        "node_name": NODES[2]['name'],
        "node_os": "Linux Ubuntu Server 14.04",
        "enabled_plugins": PLUGINS,
    }
]

plugins_info = [
    {
        "plugin_name": PLUGINS[0],
        "description": u"Плагин для сбора с узла информации о загрузке процессора",
    },
    {
        "plugin_name": PLUGINS[1],
        "description": u"Плагин для сбора с узла информации о загрузке оперативной памяти",
    },
    {
        "plugin_name": PLUGINS[2],
        "description": u"Плагин для сбора с узла информации о загрузке жесткого диска",
    },
]

params_info = [
    # CPU load plugin's params
    {
        "plugin_name": PLUGINS[0],
        "param_name": "cpu_percent",
        "description": u"Описание параметра cpu_load",
        "timeout": 10,
        "axis_y_title": "CPU's % load",
        "axis_x_title": "Time line",
        "graph_type": "line_chart"
    },
    # RAM usage plugin's params
    {
        "plugin_name": PLUGINS[1],
        "param_name": "virtual_memory",
        "description": u"Описание параметра ram_usage",
        "timeout": 10,
        "axis_y_title": "RAM's % usage",
        "axis_x_title": "Time line",
        "graph_type": "line_chart"
    },
    # HDD usage plugin's params
    {
        "plugin_name": PLUGINS[2],
        "param_name": "disk_usage",
        "description": u"Описание параметра hdd_usage",
        "timeout": 3600,
        "axis_y_title": "Mega bytes usage",
        "axis_x_title": "Time line",
        "graph_type": "pie_chart"
    },
]


save_nodes_info(nodes_info)
save_params_info(params_info)
save_plugins_info(plugins_info)
save_node_groups(NODE_GROUPS)