from django.conf.urls import url
from django.contrib import admin
from suggestionsapp import views

urlpatterns = [
    url(r'^$', views.SuggestionsListView.as_view(), name='suggestions-list'),
]
