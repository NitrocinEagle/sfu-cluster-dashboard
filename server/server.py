import jsonrpclib
from mongoengine import connect
from tornado import ioloop
from models import *
import time


def get_data_from_node(server, node_ip, node_name, plugin_name, param_name):
    def callback():
        method_name = plugin_name + '~' + param_name
        endpoint = getattr(server, method_name)
        print "Getting data from http://" + node_ip + ":3001"
        try:
            result = endpoint()
            print "%s - %s - %s: " % (node_ip, plugin_name, param_name), result
        except:
            print "Couldn't get ", param_name, " from ", node_ip
            # print 'result from ', server, ' - ', node_ip, ' - ', node_name

            # node_data = NodeData()
            # node_data.node_name = node_name
            # node_data.node_ip = node_ip
            # # TODO: parameter can be not equal to the name of plugin
            # node_data.param_name = plugin_name
            # node_data.plugin_name = plugin_name
            # data = LineChartMetric()
            # data.value = result['data']
            # data.timestamp = time.time()
            # node_data.data = data
            # node_data.save()

    return callback


if __name__ == "__main__":
    callbacks = []
    connect("test_monitoring")
    loop = ioloop.IOLoop.instance()

    monitoring_info = MonitoringInfo.objects()

    for info in monitoring_info:
        if info.ip == '127.0.0.1':
            server = jsonrpclib.Server('http://' + info.ip + ':3002')
            kwargs = {
                'server': server,
                'node_ip': info.ip,
                'node_name': info.node,
                'plugin_name': info.plugin,
                'param_name': info.param
            }
            timeout = 1000 * info.timeout
            callbacks.append(
                ioloop.PeriodicCallback(get_data_from_node(**kwargs), timeout,
                                        loop))

    map(lambda callback: callback.start(), callbacks)
    loop.start()
