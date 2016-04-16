# -*- coding: utf-8 -*-
from app.mongo_models import NodeInfo, NodeGroups
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
            'node_ip': self.form_data['node_ip'][0],
            'node_name': self.form_data['node_name'][0],
            'node_os': self.form_data['node_os'][0],
            'enabled_plugins': self.form_data['plugins_list'],
        }
        new_node_info = NodeInfo(**data)
        # new_node_info.save()
        return new_node_info


class AddServerGroupHandler(FormHandler):
    require_fields = ['group_name']

    def handle(self):
        data = {
            'name': self.form_data['group_name'],
            'enabled_nodes': None
        }
        all_groups = NodeGroups.objects()
        for g in all_groups:
            if g.name == data['name']:
                raise forms.ValidationError(self.valid_msg['group_exist'])
        new_group = NodeGroups(**data)
        # new_group.save()
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
        print 'enabled_nodes before: ', enabled_nodes
        if selected_node in enabled_nodes:
            del enabled_nodes[enabled_nodes.index(selected_node)]
        print 'enabled_nodes after: ', enabled_nodes
        group.update(enabled_nodes=enabled_nodes)
        return True
