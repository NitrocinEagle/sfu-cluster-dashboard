# -*- coding: utf-8 -*-
from django import forms
from django.utils.safestring import mark_safe
from app.mongo_models import NodeInfo

ATTRS = {'class': 'form-control'}
NODES_LIST = [(item.node_name, item.node_name) for item in NodeInfo.objects()]

class CheckboxSelectMultiple(forms.CheckboxSelectMultiple):
    def render(self, name, value, attrs=None, choices=()):
        html = super(CheckboxSelectMultiple, self).render(name, value, attrs,
                                                          choices)

        return mark_safe(html.replace('<ul>', '<ul class="myClass">'))


class ShowGraphForm(forms.Form):
    select_node = forms.ChoiceField(choices=NODES_LIST,
                                    widget=forms.Select(attrs=ATTRS),
                                    required=True,
                                    label=u'Выберите узел')
    select_plugin = forms.ChoiceField(widget=forms.Select(attrs=ATTRS),
                                      required=True,
                                      label=u'Выберите плагин')
    select_param = forms.ChoiceField(widget=forms.Select(attrs=ATTRS),
                                     required=True,
                                     label=u'Выберите параметр')
