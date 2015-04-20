#!/usr/bin/python
# -*- coding:utf-8 -*-
# Filename: 'urls.py'

"""Documentation"""

from django.conf.urls import include, url
from user.views import UserDetailView, UserBasicView, UserPasswordView

urlpatterns = [
    url(r'^$', UserDetailView.as_view(), name="user_detail"),
    url(r'^basic/', UserBasicView.as_view(), name="user_basic"),
    url(r'^password/', UserPasswordView.as_view(), name="user_password"),

]

if __name__ == "__main__":
    pass