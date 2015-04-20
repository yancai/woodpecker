#!/usr/bin/python
# -*- coding:utf-8 -*-
# Filename: 'views.py'
# Author:   'yancai'
# Date:     '2015/4/6'

"""Documentation"""
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from login.forms import LoginForm


class IndexView(View):
    def get(self, request):
        return render(request, "woodpecker/index.html", {
            "login_form": LoginForm()
        })
    pass


class TestView(View):

    def get(self, request):
        return render(request, "test.html")

if __name__ == "__main__":
    pass