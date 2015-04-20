#!/usr/bin/python
# -*- coding:utf-8 -*-
# Filename: 'models.py'

"""Documentation"""
from django.db import models
from dict.models import ContrastType, TaskType
from user.models import User


class Task(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    task_status = models.CharField(max_length=255, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    hours = models.FloatField(blank=True, null=True)
    task_type = models.ForeignKey(TaskType, db_column='task_type', blank=True, null=True)
    describe = models.CharField(max_length=1023, blank=True, null=True)
    finish_date = models.DateField(blank=True, null=True)
    finish_time = models.TimeField(blank=True, null=True)
    spent_hours = models.CharField(max_length=255, blank=True, null=True)
    value = models.IntegerField(blank=True, null=True)
    rating = models.CharField(max_length=255, blank=True, null=True)
    contrast_type = models.ForeignKey(ContrastType, db_column='contrast_type', blank=True, null=True)
    contrast_analysis = models.CharField(max_length=255, blank=True, null=True)
    users = models.ManyToManyField(User)

    def __unicode__(self):
        return u"%s" % self.name

    class Meta:
        managed = False
        db_table = 'task'

if __name__ == "__main__":
    pass