from django.shortcuts import render
from django.views.generic import ListView, DetailView
from suggestionsapp import models


class SuggestionsListView(ListView):
    model = models.Suggestion
    template_name = 'suggestionsapp/home.html'


class SuggestionDetailView(DetailView):
    model = models.Suggestion
    template_name = 'suggestionsapp/suggestion.html'