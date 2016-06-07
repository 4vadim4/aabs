from django.db import models
from aabs.settings import MEDIA_ROOT
from django.contrib.auth.models import User
import os
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.signals import user_logged_out
import logging




class CASBook(models.Model):
    class Meta:
        db_table = "CASBook"
        verbose_name = _("CAS SRI")
        verbose_name_plural = _("CAS SRI")

    casbook_stand = models.CharField(max_length=10, verbose_name=_('Stand'))
    casbook_resource = models.CharField(max_length=20, blank=True, null=True, verbose_name=_('Informative resource'))
    casbook_name = models.CharField(max_length=20, blank=True, null=True, verbose_name=_('Server name'))
    casbook_ke = models.CharField(max_length=15, verbose_name=_('Configuration item'))
    casbook_ip = models.CharField(max_length=20, verbose_name=_('IP adress'))
    casbook_url = models.CharField(max_length=100, verbose_name=_('URL adress'))
    casbook_login = models.CharField(max_length=20, verbose_name=_('Login'))
    casbook_passwd = models.CharField(max_length=20, verbose_name=_('Password'))


    def __str__(self):
        return self.casbook_ke


class LoadFileForm(models.Model):
    class Meta:
        db_table = "LoadFileForm"
        verbose_name = _("CAS SRI file")
        verbose_name_plural = _("CAS SRI files")

    file = models.FileField(upload_to='cas_nsi/')


    def __str__(self):
        full_path = os.path.join(MEDIA_ROOT, self.file.name)
        filepathis = os.path.basename(full_path)

        return filepathis
#        return self.name()




class UserProfile(models.Model):
    user = models.OneToOneField(User)
    last_last_name = models.CharField(max_length=15, verbose_name=_('WLast name'))
#    avatar = models.ImageField(upload_to='images/users', verbose_name='Изображение')

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')




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
