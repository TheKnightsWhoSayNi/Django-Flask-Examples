# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render, render_to_response, get_object_or_404
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from annoying.decorators import render_to
from django.contrib.auth import logout
from django.contrib.auth.models import User
from .forms import UserForm,UserProfileForm
from .models import UserProfile
from django.core.context_processors import csrf

def register(request):
    registered = False
    if request.method == 'POST':
        # Берем две формы и отправляем их для заполнения
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        # Если все поля проходят валидацию, то переходим к сохранению данных
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            '''
            Зачем нужен commit=False?
            That's useful when you get most of your model data from a
            form, but need to populate some null=False fields with
            non-form data.
            Saving with commit=False gets you a model object, then you
            can add your extra data and save it.

            Создаем профиль, заполняем, добавляем связь с юзером и потом
            сохраняем данные, а также завершаем регистрацию.
            '''
            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,
            'registration_form.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print("Invalid login details: {0},{1}".format(username,password))
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'login.html')

@login_required
@render_to('edit_profile.html')
'''
Вытаскиваем форму, принадлежащую пользователю. Передаём данные и форму.
Сохраняем, если изменили всё правильно.
'''
def profile_update(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/profile/')
    else:
        user = request.user
        profile = user.profile
        form = UserProfileForm(instance=user.profile)
    args = {}
    args.update(csrf(request))
    args['form'] = form
    return args

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required
def profile_info(request):
    return render(request, 'profile.html')
