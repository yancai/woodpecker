#!/usr/bin/python
# -*- coding:utf-8 -*-
# Filename: 'views.py'

"""Documentation"""
from django.contrib.auth import login
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View
from login.forms import LoginForm


class LoginView(View):

    def post(self, request):
        form = LoginForm(request, data=request.POST)
        redirect_to = "task_list"
        if form.is_valid():
            login(request, form.get_user())
            return HttpResponseRedirect(reverse(redirect_to))

        return HttpResponse(render(request, "woodpecker/index.html", {"login_form": form}))


if __name__ == "__main__":
    pass