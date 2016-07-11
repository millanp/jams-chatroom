from channels import Group
from channels.sessions import channel_session
from django.core import serializers
from .models import Chatroom, Message
from urlparse import parse_qs
import logging

log = logging.getLogger(__name__)


@channel_session
def ws_connect(message):
    # So that localhost:5000/chat/asdfasdf2323 -> chat, asdfasdf2323
    # TODO: error handling
    log.error(message['path'].strip('/'))
    prefix, label = message['path'].strip('/').split('/')
    room = Chatroom.objects.get(label=label)
    Group('chat-' + label).add(message.reply_channel)
    message.channel_session['room'] = room.label


@channel_session
def ws_receive(message):
    # De-serialize form (it is currently sent as url)
    decoded_text = parse_qs(message['text'])['text'][0]  # the second text is in the url
    message_model = Message.objects.create(room=chtrm(message),
                                           text=decoded_text)
    Group('chat-' + message.channel_session['room']).send({'text': message_model.text})


@channel_session
def ws_disconnect(message):
    Group('chat-' + rmlabel(message)).discard(message.reply_channel)


@channel_session
def rmlabel(message):
    return message.channel_session['room']


def chtrm(message):
    return Chatroom.objects.get(label=rmlabel(message))
