import jsonrpclib
import mongoengine.connect
from tornado import ioloop
from models import *
import time


def get_data_from_node(server, node_ip, node_name, plugin_name):
    def callback():
        endpoint = getattr(server, plugin_name)
        print "Getting data from http://"+ node_ip +":3001"
        result = endpoint()
        node_data = NodeData()
        node_data.node_name = node_name
        node_data.node_ip = node_ip
        # TODO: parameter can be not equal to the name of plugin
        node_data.param_name = plugin_name
        node_data.plugin_name = plugin_name
        data = LineChartMetric()
        data.value = result['data']
        data.timestamp = time.time()
        node_data.data = data
        node_data.save()
    return callback


if __name__ == "__main__":
    callbacks = []
    mongoengine.connect('test')
    servers = {}
    loop = ioloop.IOLoop.instance()

    nodes = NodeInfo.objects()
    for node in nodes:
        node_ip = node.node_ip
        if node_ip == '127.0.0.1':
            node_name = node.node_name
            server = jsonrpclib.Server('http://' + node_ip + ':3001')
            servers[node_ip] = server
            for plugin_name in node.enabled_plugins:
                plugin = PluginInfo.objects().filter(plugin_name=plugin_name)[0]
                timeout = plugin.params_info[0].timeout
                callbacks.append(ioloop.PeriodicCallback(get_data_from_node(servers[node_ip], node_ip, node_name, plugin_name), 1000*timeout, loop))

    map(lambda callback: callback.start(), callbacks)
    loop.start()