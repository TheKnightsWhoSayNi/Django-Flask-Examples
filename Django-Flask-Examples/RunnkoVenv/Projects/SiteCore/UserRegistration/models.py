# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
'''
Собственно есть 2, известных мне, способа сделать Профиль пользователя и
Личный кабинет: Наследовать класс User и делать свой кастомный класс,
получая при этом возможность всех характерных команд для юзера типа
User.request или же добавлять OneToOne связь в класс профиля как ниже.
Лично мне этот способ кажется удобней.
'''
class UserProfile(models.Model):
    user = models.OneToOneField(User)# Связывает таблицы Юзера и Профиля
    # Два обязательных параметра Юзера помимо Email/Login/Password
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    '''
    Ниже демонстрация как можно сделать 2 типа аккаунта, если вам
    нужно разделить пользователей по функционалу, но вы не хотите
    использовать группы, честно говоря я не знаю зачем нужны группы.
    '''
    PROFILE_CHOICES = (
            ('RC', 'Recruiter'),
            ('CT', 'Candidate'),
            )
    profileType = models.CharField(max_length=255, choices = PROFILE_CHOICES)

'''
Магическая функция, которую я нашел на просторах интернета,
создает профиль пользователя если его не существует,
в любом случае вернет вам профиль.
Подробнее на ангельском про то что делает эта функция можете узнать тут:
http://www.codekoala.com/posts/quick-django-tip-user-profiles/
'''
User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
