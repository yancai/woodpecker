#!/usr/bin/python
# -*- coding:utf-8 -*-
# Filename: 'urls.py'

"""Documentation"""

from django.conf.urls import include, url
from register.views import RegisterView, SuccessView

urlpatterns = [
    url(r'^$', RegisterView.as_view(), name="register"),
    url(r'^success/', SuccessView.as_view(), name="success"),
]

if __name__ == "__main__":
    pass