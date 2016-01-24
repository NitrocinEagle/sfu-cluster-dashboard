# -*- coding: utf-8 -*-
from time import time

GRAPHS = ("line_chart", "stacked_area", "pie_chart",)

metric_example = [
    {
        "x": int(time()) + 10,
        "y": 16
    },
    {
        "x": int(time()) + 20,
        "y": 10
    },
    {
        "x": int(time()) + 30,
        "y": 23
    },
    {
        "x": int(time()) + 40,
        "y": 65
    },
    {
        "x": int(time()) + 50,
        "y": 12
    },
    {
        "x": int(time()) + 60,
        "y": 34
    },
    {
        "x": int(time()) + 70,
        "y": 26
    },
]
nodes_data_example = [
    {
        "plugin_name": "cpu_load",
        "parametres":
            [
                {
                    "param_name": "cpu_load",
                    "axis_y_title": "CPU's % load",
                    "axis_x_title": "Time line",
                    "graph_type": "line_chart",
                    "dataset": [
                        {
                            "metric_name": "CPU's % load",
                            "data": metric_example
                        },
                    ]
                }
            ],
    },
    {
        "plugin_name": "ram_usage",
        "parametres":
            [
                {
                    "param_name": "ram_usage",
                    "axis_y_title": "RAM's % usage",
                    "axis_x_title": "Time line",
                    "graph_type": "line_chart",
                    "dataset": [
                        {
                            "metric_name": "RAM's % usage",
                            "data": metric_example
                        },
                    ]
                }
            ],
    },
    {
        "plugin_name": "hdd_usage",
        "parametres":
            [
                {
                    "param_name": "hdd_usage",
                    "axis_y_title": "Mega bytes usage",
                    "axis_x_title": "Time line",
                    "graph_type": "pie_chart",
                    "dataset": [
                        {
                            "metric_name": "Avaible",
                            "data": metric_example
                        },
                        {
                            "metric_name": "Used",
                            "data": metric_example
                        },
                    ]
                }
            ],
    }
]

NODES_DATA = [
    {
        "node_name": "ULK416-cluster1-0",
        "node_ip": "127.0.0.1",
        "node_data": nodes_data_example
    },
    {
        "node_name": "ULK416-cluster1-1",
        "node_ip": "192.168.0.1",
        "node_data": nodes_data_example
    },
    {
        "node_name": "ULK416-cluster1-2",
        "node_ip": "192.168.0.2",
        "node_data": nodes_data_example
    },
]

PLUGINS_INFO = [
    {
        "plugin_name": "cpu_load",
        "description": "Плагин для сбора с узла информации о загрузке процессора",
        "parametres": [
            {
                "param_name": "cpu_load",
                "description": "Параметр 'Загрузка процессора', график представлен в виде линии, построенной на парах "
                               "значений: X - загрузка процессора в %, Y - время, в которое была такая нагрузка. Каждые"
                               "10 секунд производится сбор новой пары значений.",
                "timeout": 10
            },
        ],
    },
    {
        "plugin_name": "ram_usage",
        "description": "Плагин для сбора с узла информации о загрузке оперативной памяти",
        "parametres": [
            {
                "param_name": "ram_usage",
                "description": "Параметр 'Загрузка оперативной памяти', график представлен в виде линии, построенной на "
                               "парах значений: X - загрузка оперативной памяти в Mb, Y - время, в которое была такая "
                               "нагрузка. Каждые 10 секунд производится сбор новой пары значений.",
                "timeout": 10
            },
        ],
    },
    {
        "plugin_name": "hdd_usage",
        "description": "Плагин для сбора с узла информации о загрузке жесткого диска",
        "parametres": [
            {
                "param_name": "hdd_usage",
                "description": "Параметр 'Загрузка жесткого диска', график представлен в виде круговой диаграммы, "
                               "построенной на множестве, состоящих из пар значений: X - кол-во доступной, занятой "
                               "и всякой разной памяти в Mb, Y - время, в которое была такая нагрузка. Каждые 60 минут"
                               " производится сбор новой информации.",
                "timeout": 3600
            },
        ],
    },
]

NODES_INFO = [
    {
        "node_type": "server",  # In future there can be Rital sensor
        "node_ip": "127.0.0.1",
        "node_name": "ULK416-cluster1-0",
        "node_os": "Linux Ubuntu",
        "enabled_plugins": ["cpu_load", "ram_usage", "hdd_usage"],
    },
    {
        "node_type": "server",  # In future there can be Rital sensor
        "node_ip": "192.168.0.1",
        "node_name": "ULK416-cluster1-1",
        "node_os": "Linux Ubuntu",
        "enabled_plugins": ["cpu_load", "ram_usage", "hdd_usage"],
    },
    {
        "node_type": "server",  # In future there can be Rital sensor
        "node_ip": "192.168.0.2",
        "node_name": "ULK416-cluster1-2",
        "node_os": "Linux Ubuntu",
        "enabled_plugins": ["cpu_load", "ram_usage", "hdd_usage"],
    },
]
