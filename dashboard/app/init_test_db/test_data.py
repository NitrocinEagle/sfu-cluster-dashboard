# -*- coding: utf-8 -*-
from time import time
import random

PLUGINS = ("CPU_LOAD_PLUGIN", "RAM_USAGE_PLUGIN", "HDD_USAGE_PLUGIN")
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
        "param_name": "cpu_load",
        "description": u"Описание параметра cpu_load",
        "timeout": 10,
        "axis_y_title": "CPU's % load",
        "axis_x_title": "Time line",
        "graph_type": "line_chart"
    },
    {
        "plugin_name": PLUGINS[0],
        "param_name": "ram_usage",
        "description": u"Описание параметра ram_usage",
        "timeout": 10,
        "axis_y_title": "RAM's % usage",
        "axis_x_title": "Time line",
        "graph_type": "line_chart"
    },
    {
        "plugin_name": PLUGINS[0],
        "param_name": "hdd_usage",
        "description": u"Описание параметра hdd_usage",
        "timeout": 3600,
        "axis_y_title": "Mega bytes usage",
        "axis_x_title": "Time line",
        "graph_type": "pie_chart"
    },
    # RAM usage plugin's params
    {
        "plugin_name": PLUGINS[1],
        "param_name": "cpu_load",
        "description": u"Описание параметра cpu_load",
        "timeout": 10,
        "axis_y_title": "CPU's % load",
        "axis_x_title": "Time line",
        "graph_type": "line_chart"
    },
    {
        "plugin_name": PLUGINS[1],
        "param_name": "ram_usage",
        "description": u"Описание параметра ram_usage",
        "timeout": 10,
        "axis_y_title": "RAM's % usage",
        "axis_x_title": "Time line",
        "graph_type": "line_chart"
    },
    {
        "plugin_name": PLUGINS[1],
        "param_name": "hdd_usage",
        "description": u"Описание параметра hdd_usage",
        "timeout": 3600,
        "axis_y_title": "Mega bytes usage",
        "axis_x_title": "Time line",
        "graph_type": "pie_chart"
    },
    # HDD usage plugin's params
    {
        "plugin_name": PLUGINS[2],
        "param_name": "cpu_load",
        "description": u"Описание параметра cpu_load",
        "timeout": 10,
        "axis_y_title": "CPU's % load",
        "axis_x_title": "Time line",
        "graph_type": "line_chart"
    },
    {
        "plugin_name": PLUGINS[2],
        "param_name": "ram_usage",
        "description": u"Описание параметра ram_usage",
        "timeout": 10,
        "axis_y_title": "RAM's % usage",
        "axis_x_title": "Time line",
        "graph_type": "line_chart"
    },
    {
        "plugin_name": PLUGINS[2],
        "param_name": "hdd_usage",
        "description": u"Описание параметра hdd_usage",
        "timeout": 3600,
        "axis_y_title": "Mega bytes usage",
        "axis_x_title": "Time line",
        "graph_type": "pie_chart"
    },
]

dataset_cpu_load = []
dataset_ram_usage = []
dataset_hdd_usage = []
time_now = int(time())

for i in range(20):
    dataset_cpu_load.append(
            {
                "timestamp": time_now + i * 1000,
                "value": round(random.random() * 100, 2)
            }
    )
    dataset_ram_usage.append(
            {
                "timestamp": time_now + i * 10,
                "value": random.randint(512, 2048)
            }
    )
    dataset_hdd_usage.append(
            {
                "timestamp": time_now + i * 3600,
                "data": [
                    {
                        "sector_name": "Avaible",
                        "value": 50 * 1024,
                    },
                    {
                        "sector_name": "Used",
                        "value": 150 * 1024,
                    },
                ]
            }
    )

nodes_data = [
    # Node ULK416-cluster1-0
    {
        "node_name": NODES[0]['name'],
        "node_ip": NODES[0]['ip'],
        "plugin_name": PLUGINS[0],
        "param_name": "cpu_load",
        "data": dataset_cpu_load
    },
    {
        "node_name": NODES[0]['name'],
        "node_ip": NODES[0]['ip'],
        "plugin_name": PLUGINS[1],
        "param_name": "ram_usage",
        "data": dataset_ram_usage
    },
    {
        "node_name": NODES[0]['name'],
        "node_ip": NODES[0]['ip'],
        "plugin_name": PLUGINS[2],
        "param_name": "hdd_usage",
        "data": dataset_hdd_usage
    },
    # Node ULK416-cluster1-1
    {
        "node_name": NODES[1]['name'],
        "node_ip": NODES[1]['ip'],
        "plugin_name": PLUGINS[0],
        "param_name": "cpu_load",
        "data": dataset_cpu_load
    },
    {
        "node_name": NODES[1]['name'],
        "node_ip": NODES[1]['ip'],
        "plugin_name": PLUGINS[1],
        "param_name": "ram_usage",
        "data": dataset_ram_usage
    },
    {
        "node_name": NODES[1]['name'],
        "node_ip": NODES[1]['ip'],
        "plugin_name": PLUGINS[2],
        "param_name": "hdd_usage",
        "data": dataset_hdd_usage
    },
    # Node ULK416-cluster1-2
    {
        "node_name": NODES[2]['name'],
        "node_ip": NODES[2]['ip'],
        "plugin_name": PLUGINS[0],
        "param_name": "cpu_load",
        "data": dataset_cpu_load
    },
    {
        "node_name": NODES[2]['name'],
        "node_ip": NODES[2]['ip'],
        "plugin_name": PLUGINS[1],
        "param_name": "ram_usage",
        "data": dataset_ram_usage
    },
    {
        "node_name": NODES[2]['name'],
        "node_ip": NODES[2]['ip'],
        "plugin_name": PLUGINS[2],
        "param_name": "hdd_usage",
        "data": dataset_hdd_usage
    },
]

previews_constructor = [
    {
        "username": "test",
        "node_name": NODES[2]['name'],
        "node_ip": NODES[2]['ip'],
        "plugin_name": PLUGINS[0],
        "param_name": "cpu_load"
    },
    {
        "username": "test",
        "node_name": NODES[2]['name'],
        "node_ip": NODES[2]['ip'],
        "plugin_name": PLUGINS[2],
        "param_name": "hdd_usage"
    },
    {
        "username": "test",
        "node_name": NODES[1]['name'],
        "node_ip": NODES[1]['ip'],
        "plugin_name": PLUGINS[0],
        "param_name": "cpu_load"
    },
    {
        "username": "test",
        "node_name": NODES[0]['name'],
        "node_ip": NODES[0]['ip'],
        "plugin_name": PLUGINS[1],
        "param_name": "ram_usage"
    },
]
