from django.db import models
from aabs.settings import MEDIA_ROOT
import os



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

