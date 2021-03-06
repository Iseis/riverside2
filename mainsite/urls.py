from django.conf.urls import url, include
from django.contrib.auth.views import (
    password_reset,
    password_reset_complete,
    password_reset_confirm,
    password_reset_done,
)

from django.views.generic import TemplateView, RedirectView
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'accounts/', include('registration.backends.simple.urls')),
    url(r'^accounts/password/reset/$',
        password_reset,
        {'template_name': 'registration/password_reset_form.html'},
        name='password_reset'),
    url(r'^accounts/password/reset/done/$',
        password_reset_done,
        {'template_name': 'registration/password_reset_done.html'},
        name='password_reset_done'),
    url(r'^accounts/password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        password_reset_confirm,
        {'template_name': 'registration/password_reset_confirm.html'},
        name='password_reset_confirm'),
    url(r'^accounts/password/done/$',
        password_reset_complete,
        {'template_name': 'registration/password_reset_complete.html'},
        name='password_reset_complete'),
]