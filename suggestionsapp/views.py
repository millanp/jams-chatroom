from django.shortcuts import render
from django.views.generic import ListView
from suggestionsapp import models


class SuggestionsListView(ListView):
    model = models.Suggestion
    template_name = 'suggestionsapp/home.html'