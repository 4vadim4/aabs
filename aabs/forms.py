# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from .models import CASBook, LoadFileForm
from django.utils.translation import ugettext_lazy as _

class AddCASBook(ModelForm):
    class Meta:
        model = CASBook
        fields = ['casbook_stand', 'casbook_resource', 'casbook_name', 'casbook_ke', 'casbook_ip', 'casbook_url', 'casbook_login', 'casbook_passwd']


class AddLoadFileForm(ModelForm):
    class Meta:
        model = LoadFileForm
        fields = '__all__'

    file = forms.FileField(
        label=_('Choose the file',)
#        help_text='max. 42 Mb'
    )
