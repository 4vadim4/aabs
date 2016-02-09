# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render, render_to_response, redirect
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from django.contrib import auth
from .forms import AddCASBook, AddLoadFileForm
from .models import CASBook, LoadFileForm




def welcome(request):
    return render_to_response('welcome.html')

def home(request):
    return render_to_response('home.html')

def irbis(request):
    return render_to_response('irbis.html')


def cas_nsi(request):
    if request.method == 'POST':
        form1 = AddCASBook(request.POST)
        if form1.is_valid():
            book = CASBook.objects.create(casbook_stand = form1.cleaned_data['casbook_stand'], casbook_resource = form1.cleaned_data['casbook_resource'],
                                          casbook_name = form1.cleaned_data['casbook_name'], casbook_ke = form1.cleaned_data['casbook_ke'],
                                          casbook_ip = form1.cleaned_data['casbook_ip'], casbook_url = form1.cleaned_data['casbook_url'],
                                          casbook_login = form1.cleaned_data['casbook_login'], casbook_passwd = form1.cleaned_data['casbook_passwd'])
            book.save()
            return HttpResponseRedirect(reverse('cas_nsi'))
        else:
            form1 = AddCASBook()

#    add_data = AddCASBook
#    documents = LoadFileForm.objects.all()
    args = {}
    args.update(csrf(request))
    args['all_odjects'] = CASBook.objects.all()
    args['documents'] = LoadFileForm.objects.all()
    args['form1'] = AddCASBook()
    args['form2'] = AddLoadFileForm()
    args['username'] = auth.get_user(request).username
    return render_to_response('cas_nsi.html', args, context_instance=RequestContext(request))


def cas_nsi_load(request):
    if request.method == 'POST':
        form2 = AddLoadFileForm(request.POST, request.FILES)
        if form2.is_valid():
            newdoc = LoadFileForm(file = request.FILES['file'])
            newdoc.save()
            return HttpResponseRedirect(reverse('cas_nsi_load'))

    else:
        form2 = AddLoadFileForm()

#    documents = LoadFileForm.objects.all()
#    return render_to_response('cas_nsi.html', {'documents': documents, 'form': form}, context_instance=RequestContext(request))
    args = {}
    args.update(csrf(request))
    args['all_odjects'] = CASBook.objects.all()
    args['documents'] = LoadFileForm.objects.all()
    args['form1'] = AddCASBook()
    args['form2'] = AddLoadFileForm()
    args['username'] = auth.get_user(request).username
    return render_to_response('cas_nsi.html', args, context_instance=RequestContext(request))






def kc(request):
    return render_to_response('kc.html')


def vik(request):
    return render_to_response('vik.html')




def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            args['login_error'] = "Пользователь не найден"
            return render_to_response('login.html', args)

    else:
        return render_to_response('login.html', args)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('home'))