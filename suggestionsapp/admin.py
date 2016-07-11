from django.contrib import admin
from suggestionsapp.models import Suggestion, Chatroom, Message


admin.site.register(Suggestion)
admin.site.register(Chatroom)
admin.site.register(Message)
