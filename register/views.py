#!/usr/bin/python
# -*- coding:utf-8 -*-
# Filename: 'views.py'

"""Documentation"""
import urllib2
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView, View
from login.forms import LoginForm
from register.forms import RegisterForm
from user.models import User


class RegisterView(CreateView):

    def post(self, request, *args, **kwargs):
        uf = RegisterForm(request.POST)
        if uf.is_valid():
            try:
                User.objects.create_user(
                    email=uf.cleaned_data["email"],
                    nickname=uf.cleaned_data["nickname"],
                    password=uf.cleaned_data["password"]
                )
            except Exception as e:
                return HttpResponse(render(request, "register/register.html", {"form": uf}))

            return HttpResponseRedirect("/register/success/?email=%s" % urllib2.quote(uf.cleaned_data["email"]))
        else:
            return HttpResponse(render(request, "register/register.html", {"form": uf}))


    def get(self, request, *args, **kwargs):
        form = RegisterForm()
        return render(request, "register/register.html", {"form": form})


class SuccessView(View):

    def get(self, request):
        email = request.GET.get("email")
        form = LoginForm()
        return HttpResponse(render(request, "register/success.html", {
            "email": email,
            "login_form": form,
        }))

if __name__ == "__main__":
    pass