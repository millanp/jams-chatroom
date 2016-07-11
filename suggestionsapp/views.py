from django.views.generic import ListView, DetailView, CreateView, FormView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from suggestionsapp import models
from suggestionsapp import forms


class SuggestionsListView(ListView):
    SUGGESTIONS_DISPLAYED = 7
    model = models.Suggestion
    template_name = 'suggestionsapp/home.html'

    def get_queryset(self):
        if self.SUGGESTIONS_DISPLAYED == 'all':
            return models.Suggestion.objects.order_by('-votecount')
        else:
            return models.Suggestion.objects.order_by('-votecount')[:self.SUGGESTIONS_DISPLAYED]

    def get_context_data(self, **kwargs):
        context = super(SuggestionsListView, self).get_context_data(**kwargs)
        context['SUGGESTION_COUNT'] = models.Suggestion.objects.all().count()
        context['SUGGESTIONS_DISPLAYED'] = self.SUGGESTIONS_DISPLAYED
        return context

    def post(self, request, *args, **kwargs):
        obj = models.Suggestion.objects.get(pk=request.POST.get('pk'))
        if request.POST.get('method') == 'upvote':
            obj.upvote(request.user)
        elif request.POST.get('method') == 'downvote':
            obj.downvote(request.user)
        return HttpResponse('')


class FullSuggestionsListView(SuggestionsListView):
    template_name = 'suggestionsapp/all_suggestions.html'
    queryset = models.Suggestion.objects.order_by('-votecount')
    SUGGESTIONS_DISPLAYED = 'all'


class SuggestionDetailView(FormView, DetailView):
    model = models.Suggestion
    template_name = 'suggestionsapp/suggestion_detail.html'
    form_class = forms.PostMessageForm


class SuggestionCreateView(SuccessMessageMixin, CreateView):
    model = models.Suggestion
    template_name = 'suggestionsapp/create_suggestion.html'
    form_class = forms.SuggestionModelForm
    success_url = reverse_lazy('suggestions-partial-list')
    success_message = 'Suggestion posted!'
