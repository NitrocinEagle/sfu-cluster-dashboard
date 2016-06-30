# -*- coding: utf-8 -*-
from time import time
import random

PLUGINS = ("CPU", "RAM", "HDD")

MONITORING_INFO = [
    {
        "node": 'Localhost',
        "ip": "127.0.0.1",
        "plugin": "CPU",
        "param": "cpu_percent",
        "timeout": 0,
    },
    {
        "node": 'Localhost',
        "ip": "127.0.0.1",
        "plugin": "RAM",
        "param": "virtual_memory",
        "timeout": 0,
    },
    {
        "node": 'Localhost',
        "ip": "127.0.0.1",
        "plugin": "HDD_USAGE_PLUGIN",
        "param": "disk_usage",
        "timeout": 0,
    }
]

NODE_GROUPS = [
    {
        'name': 'localhost_group',
        'enabled_nodes': ['Localhost',]
    }
]

NODES = [
    {
        "name": "Localhost",
        "ip": "127.0.0.1"
    },
]

GRAPHS = ("line_chart", "stacked_area", "pie_chart",)

nodes_info = [
    {
        "node_name": 'Localhost',
        "node_ip": '127.0.0.1',
        "node_os": "Cent OS",
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
    {
        "plugin_name": PLUGINS[0],
        "param_name": "cpu_percent",
        "description": u"Загрузка процессора (в %)",
        "timeout": 1,
        "axis_y_title": "CPU's % load",
        "axis_x_title": "Time line",
        "graph_type": "line_chart"
    },
    {
        "plugin_name": PLUGINS[1],
        "param_name": "virtual_memory",
        "description": u"Загрузка оперативной памяти (Mb)",
        "timeout": 1,
        "axis_y_title": "RAM's % usage",
        "axis_x_title": "Time line",
        "graph_type": "line_chart"
    },
    {
        "plugin_name": PLUGINS[2],
        "param_name": "disk_usage",
        "description": u"Информация о дисковом пространстве.",
        "timeout": 3600,
        "axis_y_title": "Mega bytes usage",
        "axis_x_title": "Time line",
        "graph_type": "pie_chart"
    },
]