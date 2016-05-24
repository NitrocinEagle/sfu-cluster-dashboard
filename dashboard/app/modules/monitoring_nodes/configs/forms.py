# -*- coding: utf-8 -*-
from django import forms
from django.utils.safestring import mark_safe
from app.mongo_models import PluginInfo, NodeInfo, NodeGroups

from django.forms.utils import flatatt
from django.utils.html import format_html

MONITORING_SETTINGS_OPERATIONS = (
    ('add_node', u'Создать узел'),
    ('add_server_group', u'Добавить группу серверов'),
    ('del_server_group', u'Удалить группу серверов'),
    ('add_node_to_group', u'Добавить узел в группу серверов'),
    ('del_node_from_group', u'Удалить узел из группы серверов'),
    ('add_node_to_monitor', u'Начать мониторить узел'),
    ('stop_to_monitor_node', u'Перестать мониторить узел'),
    ('stop_to_monitor_param', u'Перестать мониторить параметр у узла'),
    ('change_param_timeout', u'Поменять таймоут параметра'),
)


class IntegerWidget(forms.Widget):
    def render(self, name, value, attrs=None):
        if value is None:
            value = ''
        final_attrs = self.build_attrs(attrs, name=name)
        for kw in self.kwargs:
            final_attrs[kw] = self.kwargs.get(kw)
        output = [format_html('<input{}>', flatatt(final_attrs))]
        output.append('</input>')
        return mark_safe('\n'.join(output))

    def __init__(self, attrs=None, **kwargs):
        self.kwargs = kwargs
        if attrs is not None:
            self.attrs = attrs.copy()
        else:
            self.attrs = {}


NODES_LIST = [(item.node_name, item.node_name) for item in NodeInfo.objects()]

ATTRS = {'class': 'form-control'}

PLUGINS_LIST = [(item.plugin_name, item.plugin_name) for item in
                PluginInfo.objects()]

GROUPS_LIST = [(item.name, item.name) for item in NodeGroups.objects()]


class CheckboxSelectMultiple(forms.CheckboxSelectMultiple):
    def render(self, name, value, attrs=None, choices=()):
        html = super(CheckboxSelectMultiple, self).render(name, value, attrs,
                                                          choices)

        return mark_safe(html.replace('<ul>', '<ul class="myClass">'))


class MonitoringSettingsForm(forms.Form):
    operation = forms.ChoiceField(choices=MONITORING_SETTINGS_OPERATIONS,
                                  widget=forms.Select(attrs=ATTRS),
                                  label=u'Операции по настройке мониторинга')
    node_name = forms.CharField(widget=forms.TextInput(attrs=ATTRS),
                                required=False,
                                label=u'Имя узла')
    node_os = forms.CharField(widget=forms.TextInput(attrs=ATTRS),
                              required=False,
                              label=u'Операционная система')
    node_ip = forms.GenericIPAddressField(widget=forms.TextInput(attrs=ATTRS),
                                          required=False,
                                          label=u'IP-адресс')
    plugins_list = forms.MultipleChoiceField(choices=PLUGINS_LIST,
                                             widget=CheckboxSelectMultiple,
                                             label=u'Выберите плагины',
                                             required=False)
    group_name = forms.CharField(widget=forms.TextInput(attrs=ATTRS),
                                 required=False,
                                 label=u'Имя группы')
    select_group = forms.ChoiceField(widget=forms.Select(attrs=ATTRS),
                                     required=False,
                                     label=u'Выберите группу серверов')
    select_node = forms.ChoiceField(choices=NODES_LIST,
                                    widget=forms.Select(attrs=ATTRS),
                                    required=False,
                                    label=u'Выберите узел')
    select_plugin = forms.ChoiceField(widget=forms.Select(attrs=ATTRS),
                                      required=False,
                                      label=u'Выберите плагин')
    select_param = forms.ChoiceField(widget=forms.Select(attrs=ATTRS),
                                     required=False,
                                     label=u'Выберите параметр')
    timeout = forms.IntegerField(required=False, label=u'Таймаут',
                                 widget=IntegerWidget(attrs={
                                     'type': 'number',
                                     'class': 'form-control'
                                 }, min_value=0))
