from mongoengine import connect
from data import *
from ..mongo_models import *

connect("test_monitoring")

def init_db():
    def save_plugins_info(plugins_info):
        for plugin in plugins_info:
            new_plugin = PluginInfo()
            new_plugin.plugin_name = plugin['plugin_name']
            new_plugin.description = plugin['description']

            if not PluginInfo.objects(plugin_name=plugin['plugin_name']).first():
                new_plugin.save()

    def save_nodes_info(nodes_info):
        for node in nodes_info:
            new_node = NodeInfo(
                node_ip=node['node_ip'],
                node_name=node['node_name'],
                node_os=node['node_os'],
                enabled_plugins=node['enabled_plugins']
            )
            if not NodeInfo.objects(node_name=node['node_name']).first():
                new_node.save()

    def save_params_info(params_info):
        for param in params_info:
            new_param = ParamInfo(
                plugin_name=param['plugin_name'],
                param_name=param['param_name'],
                description=param['description'],
                axis_y_title=param['axis_y_title'],
                axis_x_title=param['axis_x_title'],
                graph_type=param['graph_type'],
                timeout=param['timeout'],
            )
            if not ParamInfo.objects(
                    param_name=param['param_name'],
                    plugin_name=param['plugin_name']).first():
                new_param.save()

    def save_node_groups(groups):
        for group in groups:
            new_group = NodeGroups(name=group['name'],
                                   enabled_nodes=group['enabled_nodes'])
            if not NodeGroups.objects(name=group['name']):
                new_group.save()

    def save_monitoring_info(monitoring_info):
        for info in monitoring_info:
            new_info = MonitoringInfo(node=info['node'], ip=info['ip'],
                                      plugin=info['plugin'], param=info['param'],
                                      timeout=info['timeout'])
            if not MonitoringInfo.objects(node=info['node'], ip=info['ip'],
                                          plugin=info['plugin'], param=info['param'],
                                          timeout=info['timeout']):
                new_info.save()

    save_nodes_info(nodes_info)
    save_params_info(params_info)
    save_plugins_info(plugins_info)
    save_node_groups(NODE_GROUPS)
    save_monitoring_info(MONITORING_INFO)

    print '[OK] Database has been initialized'
