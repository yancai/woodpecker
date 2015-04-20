#!/usr/bin/python
# -*- coding:utf-8 -*-
# Filename: 'urls.py'

"""Documentation"""
from django.conf.urls import include, url
from task.views import TaskListView, TaskDetailView, TaskAddView

urlpatterns = [
    url(r'^$', TaskListView.as_view(), name="task_list"),
    url(r'(?P<pk>\d+)/', TaskDetailView.as_view(), name="task_detail"),
    url(r'^add/', TaskAddView.as_view(), name="task_add"),
]

if __name__ == "__main__":
    pass