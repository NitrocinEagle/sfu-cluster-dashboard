import jsonrpclib
from mongoengine import connect
from tornado import ioloop
from mongo_models import *
from datetime import datetime
import time


def get_data_from_node(server, node_ip, node_name, plugin_name, param_name):
    def callback():
        method_name = plugin_name + '~' + param_name
        endpoint = getattr(server, method_name)
        print "Getting data from http://" + node_ip + ":3001"
        try:
            result = endpoint()
            print "%s - %s - %s: " % (node_ip, plugin_name, param_name), result
            kwargs = {
                'node': node_name,
                'plugin': plugin_name,
                'param': param_name
            }
            data = MonitoringNodesData.objects(**kwargs)
            kwargs.update({
                'data': result,
                'stamp': time.mktime(datetime.now().timetuple())
            })
            MonitoringNodesData(**kwargs).save()
        except:
            print "Couldn't get ", param_name, " from ", node_ip

    return callback


def start_monitoring_nodes():
    callbacks = []
    connect("test_monitoring")
    loop = ioloop.IOLoop.instance()

    for info in MonitoringInfo.objects():
        server = jsonrpclib.Server('http://' + info.ip + ':3002')
        kwargs = {
            'server': server,
            'node_ip': info.ip,
            'node_name': info.node,
            'plugin_name': info.plugin,
            'param_name': info.param
        }
        timeout = 1000 * info.timeout
        callbacks.append(ioloop.PeriodicCallback(
            get_data_from_node(**kwargs), timeout, loop))

    map(lambda callback: callback.start(), callbacks)
    print 'Starting monitoring nodes...'
    loop.start()
