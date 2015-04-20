#!/usr/bin/python
# -*- coding:utf-8 -*-
# Filename: 'models.py'

"""Documentation"""
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):

    def create_user(self, email, password, nickname=None):
        if not email:
            raise ValueError("User mast have an email address")
        user = self.model(
            email=self.normalize_email(email),
            nickname=nickname,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.CharField(unique=True, max_length=50)
    nickname = models.CharField(max_length=255, blank=True, null=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = "email"

    def validate_password(self, plain_password):
        return plain_password == self.password

    # def is_staff(self):
    #     return self.is_admin

    class Meta:
        managed = False
        db_table = 'user'

if __name__ == "__main__":
    pass