# -*- coding: utf8 -*-
from __future__ import absolute_import
from django.views.generic import TemplateView
from app.mongo_models import NodeGroups


class GroupsView(TemplateView):
    template_name = "site/modules/monitoring_nodes/groups/groups.html"

    def get_context_data(self, **kwargs):
        kwargs['groups'] = NodeGroups.objects()
        return super(GroupsView, self).get_context_data(**kwargs)
