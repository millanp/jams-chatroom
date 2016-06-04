from __future__ import unicode_literals

from django.db import models
from django.conf import settings


class Chatroom(models.Model):
    pass


class Suggestion(models.Model):
    title = models.CharField(max_length=170)
    description = models.TextField()
    upvoters = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='upvoters', blank=True)
    downvoters = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='downvoters', blank=True)
    votecount = models.IntegerField(default=0)
    chatroom = models.ForeignKey(Chatroom, on_delete=models.CASCADE, null=True, blank=True)
