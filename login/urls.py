#!/usr/bin/python
# -*- coding:utf-8 -*-
# Filename: 'urls.py'

"""Documentation"""
from django.conf.urls import include, url
from django.contrib.auth.views import logout
from login.views import LoginView

urlpatterns = [
    url(r'^$', LoginView.as_view(), name="login"),
    url(r'^logout/', logout, {
        "next_page": "/",
        "redirect_field_name": "/"},
        name="logout"),
]

if __name__ == "__main__":
    pass