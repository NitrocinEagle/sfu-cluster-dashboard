# -*- coding: utf-8 -*-
from time import time
import random

GRAPHS = ("line_chart", "stacked_area", "pie_chart",)
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

params_decription = [
    {
        "param_name": "cpu_load",
        "axis_y_title": "CPU's % load",
        "axis_x_title": "Time line",
        "graph_type": "line_chart"
    },
    {
        "param_name": "ram_usage",
        "axis_y_title": "RAM's % usage",
        "axis_x_title": "Time line",
        "graph_type": "line_chart"
    },
    {
        "param_name": "hdd_usage",
        "axis_y_title": "Mega bytes usage",
        "axis_x_title": "Time line",
        "graph_type": "pie_chart"
    }
]

dataset_cpu_load = []
dataset_ram_usage = []
dataset_hdd_usage = []
time_now = int(time())

for i in range(10):
    dataset_cpu_load.append(
        {
            "timestamp": time_now + i * 10,
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

params_data = [
    {
        "param_description": params_decription[0],
        "dataset": dataset_cpu_load
    },
    {
        "param_description": params_decription[1],
        "dataset": dataset_ram_usage
    },
    {
        "param_description": params_decription[2],
        "dataset": dataset_hdd_usage
    }
]

plugin_data_list = [
    {
        "plugin_name": "cpu_load",
        "params_data": params_data[0]
    },
    {
        "plugin_name": "ram_usage",
        "params_data": params_data[1]
    },
    {
        "plugin_name": "hdd_usage",
        "params_data": params_data[2]
    }
]

nodes_data = [
    {
        "node_name": "ULK416-cluster1-0",
        "node_ip": "127.0.0.1",
        "node_data": plugin_data_list[0]
    },
    {
        "node_name": "ULK416-cluster1-1",
        "node_ip": "192.168.0.1",
        "node_data": plugin_data_list[1]
    },
    {
        "node_name": "ULK416-cluster1-2",
        "node_ip": "192.168.0.2",
        "node_data": plugin_data_list[2]
    },
]
print dataset_hdd_usage
print dataset_ram_usage
print dataset_cpu_load
