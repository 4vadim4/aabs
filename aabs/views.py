# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.shortcuts import render, render_to_response, redirect
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from django.contrib import auth
from .forms import AddCASBook, AddLoadFileForm
from .models import CASBook, LoadFileForm
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import (REDIRECT_FIELD_NAME, login as auth_login,
    logout as auth_logout, get_user_model, update_session_auth_hash)
from django.shortcuts import resolve_url
from django.utils.http import is_safe_url
from django.contrib.sites.shortcuts import get_current_site
from django.template.response import TemplateResponse
from django.utils.translation import ugettext as _
from django.db.models import Q
from .script import *
from django.contrib.auth.models import User



def home(request):
    persons = User.objects.all().order_by('last_name')
    log_func(request)
    return render_to_response('home.html', {'persons': persons})


def irbis(request):
    return render_to_response('irbis.html')


def cas_nsi(request):
    log_func(request)
    if request.method == 'POST':
        form1 = AddCASBook(request.POST)
        if form1.is_valid():
            book = CASBook.objects.create(casbook_stand = form1.cleaned_data['casbook_stand'], casbook_resource = form1.cleaned_data['casbook_resource'],
                                          casbook_name = form1.cleaned_data['casbook_name'], casbook_ke = form1.cleaned_data['casbook_ke'],
                                          casbook_ip = form1.cleaned_data['casbook_ip'], casbook_url = form1.cleaned_data['casbook_url'],
                                          casbook_login = form1.cleaned_data['casbook_login'], casbook_passwd = form1.cleaned_data['casbook_passwd'])
#            book.save()
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
    args['nowpath'] = request.path
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

    args = {}
    args.update(csrf(request))
    args['all_odjects'] = CASBook.objects.all()
    args['documents'] = LoadFileForm.objects.all()
    args['form1'] = AddCASBook()
    args['form2'] = AddLoadFileForm()
    args['username'] = auth.get_user(request).username

    return render_to_response('cas_nsi.html', args, context_instance=RequestContext(request))


def select_action(request):
    if request.POST:
        if 'delete' in request.POST:
            CASBook.objects.filter(casbook_ke=request.POST['select1']).delete()
            return HttpResponseRedirect(reverse('cas_nsi'))

        elif 'edit' in request.POST:
            cas_object = CASBook.objects.get(casbook_ke=request.POST['select1'])
            username = auth.get_user(request).username
            data = {'casbook_stand': cas_object.casbook_stand, 'casbook_resource': cas_object.casbook_resource,
                    'casbook_name': cas_object.casbook_name, 'casbook_ke': cas_object.casbook_ke,
                    'casbook_ip': cas_object.casbook_ip, 'casbook_url': cas_object.casbook_url,
                    'casbook_login': cas_object.casbook_login, 'casbook_passwd': cas_object.casbook_passwd
                    }
            cas_object_id = cas_object.id
            form_edit = AddCASBook(data)
            return render_to_response('cas_nsi_edit.html', {'form_edit': form_edit, 'cas_object_id': cas_object_id,
                                                            'username': username}, context_instance=RequestContext(request))



def edit_form(request, cas_object_id):
    my_record = CASBook.objects.get(id=cas_object_id)
    form_3 = AddCASBook(request.POST, instance=my_record)
    if form_3.is_valid():
        form_3.save()

    return redirect('/cas_nsi/')




def kc(request):
    return render_to_response('kc.html')


def vik(request):
    return render_to_response('vik.html')


#next function taken from the standard django package in /site-packages/django/contrib/auth/
def logout(request, next_page=None,
           template_name='logged_out.html',
           redirect_field_name=REDIRECT_FIELD_NAME,
           current_app=None, extra_context=None):
    """
        Logs out the user and displays 'You are logged out' message.
    """
    auth_logout(request)

    if next_page is not None:
        next_page = resolve_url(next_page)

    if (redirect_field_name in request.POST or
            redirect_field_name in request.GET):
        next_page = request.POST.get(redirect_field_name,
                                     request.GET.get(redirect_field_name))
        # Security check -- don't allow redirection to a different host.
        if not is_safe_url(url=next_page, host=request.get_host()):
            next_page = request.path

    if next_page:
        # Redirect to this page until the session has been cleared.
        return HttpResponseRedirect(next_page)

    current_site = get_current_site(request)
    context = {
        'site': current_site,
        'site_name': current_site.name,
        'title': _('Logged out')
    }
    if extra_context is not None:
        context.update(extra_context)
    return TemplateResponse(request, template_name, context,
        current_app=current_app)



def search(request):
    log_func(request)
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        search_search = CASBook.objects.filter(Q(casbook_stand__icontains=q) | Q(casbook_resource__icontains=q) |
                                               Q(casbook_name__icontains=q) | Q(casbook_ke__icontains=q) |
                                                Q(casbook_ip__icontains=q))
        return render_to_response('search.html', {'search_search': search_search, 'query': q})
    else:
        message = 'You submitted an empty form.'
    return render_to_response('search.html', {'message': message})



