# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CASBook',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('casbook_stand', models.CharField(max_length=10, verbose_name='Стенд')),
                ('casbook_resource', models.CharField(max_length=20, null=True, verbose_name='Информационный ресурс', blank=True)),
                ('casbook_name', models.CharField(max_length=20, null=True, verbose_name='Имя машины', blank=True)),
                ('casbook_ke', models.CharField(max_length=15, verbose_name='КЭ')),
                ('casbook_ip', models.CharField(max_length=20, verbose_name='IP адрес')),
                ('casbook_url', models.CharField(max_length=100, verbose_name='URL адрес')),
                ('casbook_login', models.CharField(max_length=20, verbose_name='Логин')),
                ('casbook_passwd', models.CharField(max_length=20, verbose_name='Пароль')),
            ],
            options={
                'db_table': 'CASBook',
                'verbose_name': 'ЦАС НСИ',
                'verbose_name_plural': 'ЦАС НСИ',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LoadFileForm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', models.FileField(upload_to='cas_nsi/')),
            ],
            options={
                'db_table': 'LoadFileForm',
                'verbose_name': 'ЦАС НСИ файлы',
                'verbose_name_plural': 'ЦАС НСИ файлы',
            },
            bases=(models.Model,),
        ),
    ]
