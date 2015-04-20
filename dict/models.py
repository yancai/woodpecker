#!/usr/bin/python
# -*- coding:utf-8 -*-
# Filename: 'models.py'

"""Documentation"""
from django.db import models


class TaskType(models.Model):
    code = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'task_type'


class ContrastType(models.Model):
    code = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contrast_type'


if __name__ == "__main__":
    pass