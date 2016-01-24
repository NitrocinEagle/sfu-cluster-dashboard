# -*- coding: utf-8 -*-
from time import time
import random

GRAPHS = ("line_chart", "stacked_area", "pie_chart",)

metric_cpu_load = []
metric_rum_usage = []
metric_hdd_usage = []
time_now = int(time())

for i in range(10):
    metric_cpu_load.append(
        {
            "timestamp": time_now + i * 10,
            "value": random.random() * 100
        }
    )
    metric_rum_usage.append(
        {
            "timestamp": time_now + i * 10,
            "value": random.randint(512, 2048)
        }
    )
    metric_hdd_usage.append(
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
                            "data": metric_cpu_load
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
                            "data": metric_rum_usage
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
                    "dataset": metric_hdd_usage
                }
            ],
    }
]


"""
Здесь хранятся данные мониторинга для каждого узла. В каждом наборе данных определены:
1. Имя узла;
2. Ip-адрес узла;
3. Собранные данные. (формат собранных данных описан выше)
"""
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
