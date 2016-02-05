# -*- coding: utf-8 -*-
__author__ = 'mist'
from dashboard.app.models import *
from mongoengine import connect
from helpers import get_dataset

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


def setting_test_node_general_info(nodes):
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


def setting_test_nodes_data(nodes_data):
    node_data_list = []
    for node_data in nodes_data:
        # NodeData()
        new_node_data = NodeData()
        new_node_data.node_name = node_data['node_name']
        new_node_data.node_ip = node_data['node_ip']
        new_node_data.plugin_data_list = []
        # PluginData
        plugins_data = node_data['node_data']
        for plugin_data in plugins_data:
            new_plugin_data = PluginData()
            new_plugin_data.plugin_name = plugin_data['plugin_name']
            new_plugin_data.param_data_list = []
            # ParamData
            params_data = plugin_data['params_data']
            for param_data in params_data:
                param_data_desription = param_data['param_description']
                new_param_data = ParamData()
                # ParamDescription
                new_param_description = ParamDescription(
                    param_name=param_data_desription['param_name'],
                    axis_y_title=param_data_desription['axis_y_title'],
                    axis_x_title=param_data_desription['axis_x_title'],
                    graph_type=param_data_desription['graph_type']
                )
                new_param_data.param_description = new_param_description

                new_param_data.dataset = get_dataset(
                    param_data_desription['graph_type'],
                    param_data['dataset']
                )
                new_plugin_data.param_data_list.append(new_param_data)
            new_node_data.plugin_data_list.append(new_plugin_data)
        node_data_list.append(new_node_data)
        if NodeData.objects() is []:
            new_node_data.save()


def setting_test_nodes_data_old(nodes_data):
    node_data_list = []
    for node_data in nodes_data:
        # NodeData()
        new_node_data = NodeData()
        new_node_data.node_name = node_data['node_name']
        new_node_data.node_ip = node_data['node_ip']
        new_node_data.plugin_data_list = []
        # PluginData
        plugins_data = node_data['node_data']
        for plugin_data in plugins_data:
            new_plugin_data = PluginData()
            new_plugin_data.plugin_name = plugin_data['plugin_name']
            new_plugin_data.param_data_list = []
            # ParamData
            params_data = plugin_data['params_data']
            for param_data in params_data:
                param_data_desription = param_data['param_description']
                new_param_data = ParamData()
                # ParamDescription
                new_param_description = ParamDescription(
                    param_name=param_data_desription['param_name'],
                    axis_y_title=param_data_desription['axis_y_title'],
                    axis_x_title=param_data_desription['axis_x_title'],
                    graph_type=param_data_desription['graph_type']
                )
                new_param_data.param_description = new_param_description

                new_param_data.dataset = get_dataset(
                    param_data_desription['graph_type'],
                    param_data['dataset']
                )
                new_plugin_data.param_data_list.append(new_param_data)
            new_node_data.plugin_data_list.append(new_plugin_data)
        node_data_list.append(new_node_data)
        if NodeData.objects() is []:
            new_node_data.save()

def setting_test_nodes_data(nodes_data):
    node_data_list = []
    for node_data in nodes_data:
        # NodeData()
        new_node_data = NodeData()
        new_node_data.node_name = node_data['node_name']
        new_node_data.node_ip = node_data['node_ip']
        new_node_data.plugin_name = node_data['plugin_name']
        new_node_data.param_name = node_data['param_name']
        # data
        data = node_data['data']
        if "timestamp" in data:

        """for plugin_data in plugins_data:
            new_plugin_data = PluginData()
            new_plugin_data.plugin_name = plugin_data['plugin_name']
            new_plugin_data.param_data_list = []
            # ParamData
            params_data = plugin_data['params_data']
            for param_data in params_data:
                param_data_desription = param_data['param_description']
                new_param_data = ParamData()
                # ParamDescription
                new_param_description = ParamDescription(
                    param_name=param_data_desription['param_name'],
                    axis_y_title=param_data_desription['axis_y_title'],
                    axis_x_title=param_data_desription['axis_x_title'],
                    graph_type=param_data_desription['graph_type']
                )
                new_param_data.param_description = new_param_description

                new_param_data.dataset = get_dataset(
                    param_data_desription['graph_type'],
                    param_data['dataset']
                )
                new_plugin_data.param_data_list.append(new_param_data)
            new_node_data.plugin_data_list.append(new_plugin_data)
        node_data_list.append(new_node_data)
        if NodeData.objects() is []:
            new_node_data.save()
