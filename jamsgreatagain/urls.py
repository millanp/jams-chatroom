"""jamsgreatagain URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import urls as authurls
from django.contrib.auth import views as auth_views
from suggestionsapp import urls
from suggestionsapp import forms as app_forms

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^registration/', include('dappr.urls')),
    url(r'^auth/login/', auth_views.login,
        {'authentication_form': app_forms.BSLoginForm}),
    url(r'^auth/', include(authurls)),
    url(r'^', include(urls)),
]
