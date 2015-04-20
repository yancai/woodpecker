#!/usr/bin/python
# -*- coding:utf-8 -*-
# Filename: 'views.py'

"""Documentation"""
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView, View


class UserDetailView(DetailView):
    def get(self, request, *args, **kwargs):
        return HttpResponse(render(request, "user/user_detail.html", {
            "user": request.user}))


class UserBasicView(View):

    def post(self, request):
        # TODO
        pass


class UserPasswordView(View):

    def post(self, request):
        # TODO
        pass

if __name__ == "__main__":
    pass