from django.conf.urls import url, include
from suggestionsapp import nav_urls
from suggestionsapp import views

urlpatterns = [
    url(r'^', include(nav_urls)),
    url(r'^detail/(?P<pk>\d+)/$', views.SuggestionDetailView.as_view(), name='suggestion-detail'),
]
