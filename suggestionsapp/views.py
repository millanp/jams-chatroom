from django.views.generic import ListView, DetailView, CreateView
from suggestionsapp import models
from suggestionsapp import forms


class SuggestionsListView(ListView):
    model = models.Suggestion
    template_name = 'suggestionsapp/home.html'


class SuggestionDetailView(DetailView):
    model = models.Suggestion
    template_name = 'suggestionsapp/suggestion_detail.html'


class SuggestionCreateView(CreateView):
    model = models.Suggestion
    template_name = 'suggestionsapp/create_suggestion.html'
    form_class = forms.SuggestionModelForm
