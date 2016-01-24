# -*- coding: utf-8 -*-
__author__ = 'mist'
from mongoengine import connect
from dashboard.app.dashboard.models import NodeInfo, ParametresInfo, PluginInfo

connect('test')

nodes = [
    {
        "node_type": "server",  # In future there can be Rital sensor
        "node_ip": "127.0.0.1",
        "node_name": "ULK416-cluster1-0",
        "node_os": "Red Hat Linux",
        "enabled_plugins": ["cpu_load", "ram_usage", "hdd_usage"],
    },
    {
        "node_type": "server",  # In future there can be Rital sensor
        "node_ip": "192.168.0.1",
        "node_name": "ULK416-cluster1-1",
        "node_os": "CentOS",
        "enabled_plugins": ["cpu_load", "ram_usage", "hdd_usage"],
    },
    {
        "node_type": "server",  # In future there can be Rital sensor
        "node_ip": "192.168.0.2",
        "node_name": "ULK416-cluster1-2",
        "node_os": "Linux Ubuntu Server 14.04",
        "enabled_plugins": ["cpu_load", "ram_usage", "hdd_usage"],
    }
]

plugins = [
    {
        "plugin_name": "cpu_load",
        "description": u"Плагин для сбора с узла информации о загрузке процессора",
        "params_info": [
            {
                "param_name": "cpu_load",
                "description": u"Параметр 'Загрузка процессора', график представлен в виде линии, построенной на парах значений: X - загрузка процессора в %, Y - время, в которое была такая нагрузка. Каждые 10 секунд производится сбор новой пары значений.",
                "timeout": 10
            },
        ],
    },
    {
        "plugin_name": "ram_usage",
        "description": u"Плагин для сбора с узла информации о загрузке оперативной памяти",
        "params_info": [
            {
                "param_name": "ram_usage",
                "description": u"Параметр 'Загрузка оперативной памяти', график представлен в виде линии, построенной на парах значений: X - загрузка оперативной памяти в Mb, Y - время, в которое была такая нагрузка. Каждые 10 секунд производится сбор новой пары значений.",
                "timeout": 10
            },
        ],
    },
    {
        "plugin_name": "hdd_usage",
        "description": u"Плагин для сбора с узла информации о загрузке жесткого диска",
        "params_info": [
            {
                "param_name": "hdd_usage",
                "description": u"Параметр 'Загрузка жесткого диска', график представлен в виде круговой диаграммы, построенной на множестве, состоящих из пар значений: X - кол-во доступной, занятой и всякой разной памяти в Mb, Y - время, в которое была такая нагрузка. Каждые 60 минут производится сбор новой информации.",
                "timeout": 3600
            },
        ],
    },
]

for plugin in plugins:
    new_plugin = PluginInfo()
    new_plugin.plugin_name = plugin['plugin_name']
    new_plugin.description = plugin['description']
    params_info_list = []
    for info in plugin['params_info']:
        param_info = ParametresInfo(param_name=info['param_name'],
                                    description=info['description'],
                                    timeout=info['timeout']
                                    )
        params_info_list.append(param_info)
    new_plugin.params_info = params_info_list

    if not PluginInfo.objects(plugin_name=plugin['plugin_name']).first():
        new_plugin.save()

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

plugins = PluginInfo.objects()
print plugins[0].params_info[0].description
