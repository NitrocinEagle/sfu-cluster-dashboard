# -*- coding: utf-8 -*-
from app.mongo_models import (NodeInfo, NodeGroups, MonitoringInfo, ParamInfo)
from django import forms


class FormHandler(object):
    form_data = {}
    require_fields = []
    valid_msg = {
        'default': u'Ошибка валидации',
        'empty_group': u"Пустое поле 'Имя группы'",
        'group_exist': u"Такая группа уже существует",
        'node_in_group': u"Узел уже находится в данной группе",
        'group_not_selected': u"Не выбрана группа",
    }

    def __init__(self, form_data):
        self.form_data = form_data
        if not self.valid():
            raise forms.ValidationError(self.valid_msg['default'])

    def valid(self):
        for f in self.require_fields:
            if not self.form_data.get(f):
                return False
        return True

    def handle(self):
        raise BaseException("To handle form data redefine method 'handle'. "
                            "self.form_data contains form data.")


class AddNodeHandler(FormHandler):
    require_fields = ['node_ip', 'node_name', 'node_os']

    def handle(self):
        data = {
            'node_ip': self.form_data['node_ip'],
            'node_name': self.form_data['node_name'],
            'node_os': self.form_data['node_os'],
            'enabled_plugins': self.form_data['plugins_list'],
        }
        new_node_info = NodeInfo(**data)
        new_node_info.save()
        return new_node_info


class AddServerGroupHandler(FormHandler):
    require_fields = ['group_name']

    def handle(self):
        data = {
            'name': self.form_data['group_name'],
            'enabled_nodes': None
        }
        all_groups = NodeGroups.objects()
        if data['name'] in [g.name for g in all_groups]:
            raise forms.ValidationError(self.valid_msg['group_exist'])
        new_group = NodeGroups(**data)
        new_group.save()
        return new_group


class AddNodeToGroupHandler(FormHandler):
    def handle(self):
        selected_node = self.form_data['select_node']
        selected_group = self.form_data['select_group']
        group = NodeGroups.objects(name=selected_group).first()
        enabled_nodes = group.enabled_nodes
        if selected_node in enabled_nodes:
            raise forms.ValidationError(self.valid_msg['node_in_group'])

        enabled_nodes.append(selected_node)
        group.update(enabled_nodes=enabled_nodes)
        return group.enabled_nodes


class DelServerGroupHandler(FormHandler):
    require_fields = ['select_group']

    def handle(self):
        group = NodeGroups.objects(
            name=self.form_data['select_group']).first()
        group.delete()
        return True


class DelNodeFromGroupHandler(FormHandler):
    def handle(self):
        selected_node = self.form_data['select_node']
        selected_group = self.form_data['select_group']
        group = NodeGroups.objects(name=selected_group).first()
        enabled_nodes = group.enabled_nodes
        if selected_node in enabled_nodes:
            del enabled_nodes[enabled_nodes.index(selected_node)]
        group.update(enabled_nodes=enabled_nodes)
        return True


class AddNodeToMonitorHandler(FormHandler):
    def handle(self):
        selected_node = self.form_data['select_node']
        node = NodeInfo.objects(node_name=selected_node).first()
        for plugin in node.enabled_plugins:
            for param in ParamInfo.objects(plugin_name=plugin):
                data = {
                    'node': node.node_name,
                    'ip': node.node_ip,
                    'plugin': plugin,
                    'param': param.param_name,
                    'timeout': 0
                }
                monitoring_info = MonitoringInfo(**data)
                monitoring_info.save()
        return True


class ChangeParamTimeoutHandler(FormHandler):
    require_fields = ['timeout']

    def handle(self):
        data = {
            'node': self.form_data['select_node'],
            'plugin': self.form_data['select_plugin'],
            'param': self.form_data['select_param'],
        }
        info = MonitoringInfo.objects(**data).first()
        info.update(timeout=self.form_data['timeout'])
        return True
