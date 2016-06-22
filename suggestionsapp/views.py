from django.views.generic import ListView, DetailView, CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from suggestionsapp import models
from suggestionsapp import forms


class SuggestionsListView(ListView):
    model = models.Suggestion
    template_name = 'suggestionsapp/home.html'

    # @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        obj = models.Suggestion.objects.get(pk=request.POST.get('pk'))
        # if request.POST.method
        obj.upvote(request.user)
        return HttpResponse('')


class SuggestionDetailView(DetailView):
    model = models.Suggestion
    template_name = 'suggestionsapp/suggestion_detail.html'


class SuggestionCreateView(SuccessMessageMixin, CreateView):
    model = models.Suggestion
    template_name = 'suggestionsapp/create_suggestion.html'
    form_class = forms.SuggestionModelForm
    success_url = reverse_lazy('suggestions-list')
    success_message = 'Suggestion posted!'
