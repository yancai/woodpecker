#!/usr/bin/python
# -*- coding:utf-8 -*-
# Filename: 'forms.py'

"""Documentation"""
from django import forms
from task.models import Task


class TaskAddForm(forms.Form):
    name = forms.CharField(
        required=True,
        label="任务名称：",
    )

    task_status = forms.CharField(
        required=True,
        label="任务状态：",
    )
    start_date = forms.DateField(
        required=True,
        label="起始日期：",
        widget=forms.TextInput(
            attrs={
                "data-format": "yyyy-MM-dd",
            }
        )
    )
    start_time = forms.TimeField(
        label="起始时间：",
        widget=forms.TextInput(
            attrs={
                "data-format": "hh:mm",
            }
        )
    )


class TaskDetailForm(forms.ModelForm):

    class Meta:
        model = Task
        # fields = "__all__"
        # fields = ("id", "name", "task_status", "start_date", "start_time", "task_type")
        fields = ("id", "name", "task_status", "start_date", "start_time", "end_date", "end_time", "hours", "task_type", "describe", "finish_date", "finish_time", "spent_hours", "value", "rating", "contrast_type", "contrast_analysis", "contrast_analysis")


if __name__ == "__main__":
    pass