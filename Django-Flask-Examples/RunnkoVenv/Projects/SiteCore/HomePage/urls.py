from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', 'HomePage.views.index'),
    url(r'^captcha/', include('captcha.urls')),
    url(r'contacts/$', 'HomePage.views.contact'),
]
