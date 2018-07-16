from django.db import models
from django.contrib.auth.models import User


class Users(User):
    stu_id = models.CharField(max_length=15)
    name = models.CharField(max_length=10)
    password = models.CharField(max_length=20)
    user_info = models.TextField()

    def __unicode__(self):
        return self.stu_id


class Activity(models.Model):
    title = models.CharField(max_length=20)
    datetime = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    activity_id = models.CharField(max_length=20)

    def __unicode__(self):
        return self.activity_id

