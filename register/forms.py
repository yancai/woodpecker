#!/usr/bin/python
# -*- coding:utf-8 -*-
# Filename: 'forms.py'

"""Documentation"""
from django import forms
from user.models import User


class RegisterForm(forms.Form):
    email = forms.EmailField(
        required=True,
        label="电子邮件：",
    )

    nickname = forms.CharField(
        label="昵称：",
        min_length=3,
        max_length=100
    )

    password = forms.CharField(
        required=True,
        label="密码：",
        min_length=6,
        widget=forms.PasswordInput()
    )

    re_password = forms.CharField(
        required=True,
        label="确认密码：",
        min_length=6,
        widget=forms.PasswordInput()
    )

    def clean_re_password(self):
        re_password = self.cleaned_data["re_password"]
        if self.cleaned_data["password"] != re_password:
            raise forms.ValidationError("两次密码输入不一致")

        return re_password

    def clean_email(self):
        email = self.cleaned_data["email"]
        count = User.objects.filter(email=email).count()
        if count > 0:
            raise forms.ValidationError("email已存在")

        return email

if __name__ == "__main__":
    pass