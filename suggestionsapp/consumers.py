from django.http import HttpResponse
from channels.handler import AsgiHandler
from channels import Group
from channels.sessions import channel_session
from .models import Chatroom


@channel_session
def ws_connect(message):
    prefix, label = message['path'].strip('/').split('/')
    room = Chatroom.objects.get(label=label)
    Group('chat-' + label).add(message.reply_channel)
    message.channel_session['room'] = room.label


def ws_receive(message):
    pass


def ws_disconnect(message):
    pass
