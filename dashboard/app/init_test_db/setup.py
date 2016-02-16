__author__ = 'mist'
from setups_test_data import *
from test_data import *
from helpers import get_dataset
# setting_test_node_general_info(nodes)
# setting_test_plugin_info(plugins)
# setting_test_nodes_data(nodes_data)


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

nodes_data = [
    {
        "node_name": "localhost",
        "node_ip": "127.0.0.1",
        "plugin_name": "cpu_load",
        "param_name": "cpu_load",
        "data": dataset_cpu_load
    },
    {
        "node_name": "localhost",
        "node_ip": "127.0.0.1",
        "plugin_name": "ram_usage",
        "param_name": "ram_usage",
        "data": dataset_ram_usage
    },
    {
        "node_name": "localhost",
        "node_ip": "127.0.0.1",
        "plugin_name": "hdd_usage",
        "param_name": "hdd_usage",
        "data": dataset_hdd_usage
    },
    {
        "node_name": "first",
        "node_ip": "192.168.0.1",
        "plugin_name": "cpu_load",
        "param_name": "cpu_load",
        "data": dataset_cpu_load
    },
    {
        "node_name": "first",
        "node_ip": "192.168.0.1",
        "plugin_name": "ram_usage",
        "param_name": "ram_usage",
        "data": dataset_ram_usage
    },
    {
        "node_name": "first",
        "node_ip": "192.168.0.1",
        "plugin_name": "hdd_usage",
        "param_name": "hdd_usage",
        "data": dataset_hdd_usage
    },
    {
        "node_name": "second",
        "node_ip": "192.168.0.2",
        "plugin_name": "cpu_load",
        "param_name": "cpu_load",
        "data": dataset_cpu_load
    },
    {
        "node_name": "second",
        "node_ip": "192.168.0.2",
        "plugin_name": "ram_usage",
        "param_name": "ram_usage",
        "data": dataset_ram_usage
    },
    {
        "node_name": "second",
        "node_ip": "192.168.0.2",
        "plugin_name": "hdd_usage",
        "param_name": "hdd_usage",
        "data": dataset_hdd_usage
    },
]

from dashboard.app.models import NodeData
from mongoengine import connect

connect("test")

for node_data in nodes_data:
    # NodeData()
    new_node_data = NodeData()
    new_node_data.node_name = node_data['node_name']
    new_node_data.node_ip = node_data['node_ip']
    new_node_data.plugin_name = node_data['plugin_name']
    new_node_data.param_name = node_data['param_name']
    # data
    if node_data['param_name'] == 'hdd_usage':
        new_node_data.data = get_dataset('pie_chart', node_data['data'])
    elif node_data['param_name'] == 'ram_usage':
        new_node_data.data = get_dataset('line_chart', node_data['data'])
    elif node_data['param_name'] == 'cpu_load':
        new_node_data.data = get_dataset('line_chart', node_data['data'])
    #new_node_data.save()
    #print NodeData.objects()

