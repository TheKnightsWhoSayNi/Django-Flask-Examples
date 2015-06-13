from django.conf.urls import patterns, include, url
from .views import *
from django.contrib.auth.views import password_reset

urlpatterns = patterns('',
    url(r'register/$','UserRegistration.views.register'),
    url(r'login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'logout/$', 'django.contrib.auth.views.logout', {'template_name': 'logout.html'}),
    url(r'profile/$', 'UserRegistration.views.profile_info'),
    url(r'profile/edit/$', 'UserRegistration.views.profile_update'),
    url(r'password/reset/$',
        'django.contrib.auth.views.password_reset',
        {'post_reset_redirect' : '/accounts/password/reset/done/'},
        name="password_reset"),
    (r'password/reset/done/$',
        'django.contrib.auth.views.password_reset_done'),
    (r'password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
        'django.contrib.auth.views.password_reset_confirm',
        {'post_reset_redirect' : '/accounts/password/done/'}),
    (r'password/done/$',
        'django.contrib.auth.views.password_reset_complete'),
)
