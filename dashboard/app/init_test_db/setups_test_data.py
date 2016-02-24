# -*- coding: utf-8 -*-
from dashboard.app.mongo_models import *
from mongoengine import connect
from helpers import get_dataset, PRINT

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
        if not ParamInfo.objects(param_name=param['param_name']).first():
            new_param.save()


def save_previews_constructor(previews):
    for preview in previews:
        new_preview = PreviewCostructor(
                username=preview['username'],
                node_name=preview['node_name'],
                node_ip=preview['node_ip'],
                plugin_name=preview['plugin_name'],
                param_name=preview['param_name'],
        )
        if not PreviewCostructor.objects(
                username=preview['username'],
                node_name=preview['node_name'],
                node_ip=preview['node_ip'],
                plugin_name=preview['plugin_name'],
                param_name=preview['param_name']).first():
            new_preview.save()


def save_nodes_data(nodes_data):
    for node_data in nodes_data:
        new_node_data = NodeData()
        new_node_data.node_name = node_data['node_name']
        new_node_data.node_ip = node_data['node_ip']
        new_node_data.plugin_name = node_data['plugin_name']
        new_node_data.param_name = node_data['param_name']

        if node_data['param_name'] == 'hdd_usage':
            new_node_data.data = get_dataset('pie_chart', node_data['data'])
        elif node_data['param_name'] == 'ram_usage':
            new_node_data.data = get_dataset('line_chart', node_data['data'])
        elif node_data['param_name'] == 'cpu_load':
            new_node_data.data = get_dataset('line_chart', node_data['data'])

            if not NodeData.objects(
                    node_name=node_data['node_name'],
                    plugin_name=node_data['plugin_name'],
                    param_name=node_data['param_name']).first():
                new_node_data.save()
