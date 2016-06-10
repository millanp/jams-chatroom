from django.conf.urls import url, include
from suggestionsapp import nav_urls

urlpatterns = [
    url(r'^', include(nav_urls)),
]
