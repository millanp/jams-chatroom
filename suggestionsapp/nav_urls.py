from django.conf.urls import url
from suggestionsapp import views

navurlpatterns = [
    ('Home', url(r'^$', views.SuggestionsListView.as_view(), name='suggestions-list')),
    ('Create a suggestion', url(r'^create/', views.SuggestionCreateView.as_view(), name='suggestion-create')),
]

urlpatterns = [x[1] for x in navurlpatterns]