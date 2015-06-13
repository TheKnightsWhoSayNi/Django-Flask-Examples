# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from .forms import *
from django.shortcuts import render, render_to_response, get_object_or_404
from django.core.mail import send_mail
from django.core.context_processors import csrf

def index(request):
    return render(request, 'index.html')

'''
Для теста писем можно юзать:
sudo python -m smtpd -n -c DebuggingServer localhost:25
На развернутом вам понадобиться завести smtp,самый простой - google smtp.
'''
def contact(request):
    form = ContactForm()
    if request.POST:
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'], # Тема письма
                cd['message'], # Ваш текст
                # Адрес отправителя в данном случае без адреса.
                cd.get('email', 'noreply@example.com'),
                ['my@mail.ru'], # Ваша Почта
            )
            return HttpResponseRedirect('/')
    else:
        form = ContactForm()
    return render_to_response('contact.html', {'form': form}, context_instance=RequestContext(request))
