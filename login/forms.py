#!/usr/bin/python
# -*- coding:utf-8 -*-
# Filename: 'forms.py'

"""Documentation"""
from django import forms
from django.contrib.auth import get_user_model, authenticate


class LoginForm(forms.Form):
    email = forms.EmailField(
        required=True,
        label="电子邮件：",
        widget=forms.EmailInput(
            attrs={
                "placeholder": "email",
                "class": "form-control",
            }
        )
    )

    password = forms.CharField(
        label="密码：",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "password",
                "class": "form-control",
            }
        )
    )

    # error_messages = {
    #     'invalid_login': _("Please enter a correct %(username)s and password. "
    #                        "Note that both fields may be case-sensitive."),
    #     'inactive': _("This account is inactive."),
    # }

    def __init__(self, request=None, *args, **kwargs):
        """
        The 'request' parameter is set for custom auth use by subclasses.
        The form data comes in via the standard 'data' kwarg.
        """
        self.request = request
        self.user_cache = None
        super(LoginForm, self).__init__(*args, **kwargs)

        # Set the label for the "username" field.
        UserModel = get_user_model()
        self.username_field = UserModel._meta.get_field("email")
        self.fields['email'].label = "email"
        pass


    def clean(self):
        username = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        # print("u: %s\t p: %s" % (username, password))

        if username and password:
            self.user_cache = authenticate(username=username,
                                           password=password)
            if self.user_cache is None:
                # raise forms.ValidationError(
                #     self.error_messages['invalid_login'],
                #     code='invalid_login',
                #     params={'username': self.username_field.verbose_name},
                # )
                raise forms.ValidationError("登录失败")
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data

    def confirm_login_allowed(self, user):
        """
        Controls whether the given User may log in. This is a policy setting,
        independent of end-user authentication. This default behavior is to
        allow login by active users, and reject login by inactive users.

        If the given user cannot log in, this method should raise a
        ``forms.ValidationError``.

        If the given user may log in, this method should return None.
        """
        if not user.is_active:
            raise forms.ValidationError(
                self.error_messages['inactive'],
                code='inactive',
            )

    def get_user_id(self):
        if self.user_cache:
            return self.user_cache.id
        return None

    def get_user(self):
        return self.user_cache

if __name__ == "__main__":
    pass