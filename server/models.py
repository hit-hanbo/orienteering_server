# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UsersManager(BaseUserManager):
    def create_user(self, stu_id, password=None):
        if not stu_id:
            raise ValueError("stu_id must not be empty !")
        user = self.model(stu_id=stu_id)
        user.set_password(raw_password=password)
        user.save(using=self._db)
        return user

    def create_superuser(self, stu_id, password):
        user = self.create_user(
            stu_id=stu_id,
            password=password
        )
        user._is_admin = True
        user.save(using=self._db)
        return user


class Users(AbstractBaseUser):
    stu_id = models.CharField(max_length=15, unique=True)
    name = models.CharField(max_length=10)
    # password = models.CharField(max_length=20)
    user_info = models.TextField()
    USERNAME_FIELD = "stu_id"
    is_admin = models.BooleanField(default=False)
    objects = UsersManager()

    def __str__(self):
        return self.stu_id

    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, object=None):
        return True

    def has_module_perms(self, app_label):
        return True


class Activity(models.Model):
    title = models.CharField(max_length=20)
    datetime = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    activity_id = models.CharField(max_length=20)
    activity_info = models.TextField()
    partners = models.ManyToManyField(Users)

    def __str__(self):
        return self.activity_id
