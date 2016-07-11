from __future__ import unicode_literals
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from django.conf import settings
from django.utils.crypto import get_random_string


class Chatroom(models.Model):
    title = models.CharField(max_length=182) # The max length of a suggestion title, plus 12
    label = models.SlugField(unique=True, default=get_random_string())

    def __str__(self):
        return self.title


class Message(models.Model):
    room = models.ForeignKey(Chatroom, related_name='messages', on_delete=models.CASCADE)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text.strip()

class Suggestion(models.Model):
    title = models.CharField(max_length=170)
    description = models.TextField()
    upvoters = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='upvoters', blank=True)
    downvoters = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='downvoters', blank=True)
    votecount = models.IntegerField(default=0)
    chatroom = models.ForeignKey(Chatroom, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

    def upvote(self, user):
        # self.upvoters.add(user)
        self.votecount += 1
        self.save()

    def downvote(self, user):
        self.votecount -= 1
        self.save()


@receiver(post_save, sender=Suggestion)
def create_chatroom(sender, instance, created, **kwargs):
    """Create a matching profile whenever a user object is created."""
    if created:
        print 'created'
        chatroom_title = instance.title + ': Discussion'
        instance.chatroom = Chatroom.objects.create(title=chatroom_title)
        instance.save()
