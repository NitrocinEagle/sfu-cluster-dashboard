# -*- coding: utf-8 -*-
__author__ = 'mist'
from dashboard.app.dashboard.models import *
from mongoengine import connect

connect("test")


def setting_test_plugin_info(plugins):
    for plugin in plugins:
        new_plugin = PluginInfo()
        new_plugin.plugin_name = plugin['plugin_name']
        new_plugin.description = plugin['description']
        params_info_list = []
        for info in plugin['params_info']:
            param_info = ParamGeneralInfo(param_name=info['param_name'],
                                          description=info['description'],
                                          timeout=info['timeout']
                                          )
            params_info_list.append(param_info)
        new_plugin.params_info = params_info_list

        if not PluginInfo.objects(plugin_name=plugin['plugin_name']).first():
            new_plugin.save()

    plugins = PluginInfo.objects()
    print plugins[0].params_info[0].description


def setting_test_node_info(nodes):
    for node in nodes:
        new_node = NodeInfo(
            node_type=node['node_type'],
            node_ip=node['node_ip'],
            node_name=node['node_name'],
            node_os=node['node_os'],
            enabled_plugins=node['enabled_plugins']
        )
        if not NodeInfo.objects(node_name=node['node_name']).first():
            new_node.save()

    nodes = NodeInfo.objects()
    for node in nodes:
        print 'Node ', node.node_name
        print '\tnode_type is ', node.node_type
        print '\tnode_ip is ', node.node_ip
        print '\tnode_os is ', node.node_os
        print '\tenabled_plugins: ', node.enabled_plugins



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
    node_data_list = EmbeddedDocumentListField(PluginData)