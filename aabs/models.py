from django.db import models
from aabs.settings import MEDIA_ROOT
from django.contrib.auth.models import User
import os

from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.signals import user_logged_out
import logging




class CASBook(models.Model):
    class Meta:
        db_table = "CASBook"
        verbose_name = "ЦАС НСИ"
        verbose_name_plural = "ЦАС НСИ"

    casbook_stand = models.CharField(max_length=10, verbose_name='Стенд')
    casbook_resource = models.CharField(max_length=20, blank=True, null=True, verbose_name='Информационный ресурс')
    casbook_name = models.CharField(max_length=20, blank=True, null=True, verbose_name='Имя машины')
    casbook_ke = models.CharField(max_length=15, verbose_name='КЭ')
    casbook_ip = models.CharField(max_length=20, verbose_name='IP адрес')
    casbook_url = models.CharField(max_length=100, verbose_name='URL адрес')
    casbook_login = models.CharField(max_length=20, verbose_name='Логин')
    casbook_passwd = models.CharField(max_length=20, verbose_name='Пароль')


    def __str__(self):
        return self.casbook_ke


class LoadFileForm(models.Model):
    class Meta:
        db_table = "LoadFileForm"
        verbose_name = "ЦАС НСИ файлы"
        verbose_name_plural = "ЦАС НСИ файлы"

    file = models.FileField(upload_to='cas_nsi/')


    def __str__(self):
        full_path = os.path.join(MEDIA_ROOT, self.file.name)
        filepathis = os.path.basename(full_path)

        return filepathis
#        return self.name()




class UserProfile(models.Model):
    user = models.OneToOneField(User)
    last_last_name = models.CharField(max_length=15, verbose_name='Отчество')
#    avatar = models.ImageField(upload_to='images/users', verbose_name='Изображение')

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'




def do_stuff_in(sender, user, request, **kwargs):
    log_name = User.objects.get(username = user)
    logging.basicConfig(format = '%(levelname)-8s [%(asctime)s] %(message)s', level = logging.INFO, filename = 'logger1.log')
    logging.info('authorization by %s %s %s' %(log_name.last_name, log_name.first_name, log_name.userprofile.last_last_name))


def do_stuff_out(sender, user, request, **kwargs):
    log_name = User.objects.get(username = user)
    logging.basicConfig(format = '%(levelname)-8s [%(asctime)s] %(message)s', level = logging.INFO, filename = 'logger1.log')
    logging.info('logout by %s %s %s' %(log_name.last_name, log_name.first_name, log_name.userprofile.last_last_name))

user_logged_in.connect(do_stuff_in)
user_logged_out.connect(do_stuff_out)
