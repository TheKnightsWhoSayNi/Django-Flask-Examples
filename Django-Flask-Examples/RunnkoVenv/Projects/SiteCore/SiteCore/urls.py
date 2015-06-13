from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^accounts/', include('UserRegistration.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^', include('HomePage.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
