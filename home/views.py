from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.shortcuts import *
from django.http import *
from .models import *
from .forms import *
from django.db.models import Q
from django.contrib import auth
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from .models import software_desc
from .models import win_32
from .models import win_64
from .models import mac
from .models import android
from django.shortcuts import render_to_response
from forms import subsform
from django.views.generic import CreateView
from django import forms
from django_user_agents.utils import get_user_agent
def index(request):
    if request.method=='POST':
            form=subsform(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/')
    else:
        form=subsform()

    if(PageView.objects.count()<=0):
        x=PageView.objects.create()
        x.save()
    else:
        x=PageView.objects.all()[0]
        x.hits=x.hits+1
        x.save()
    return render(request,'personal/download.html',{'form':form,'page':x.hits})

def catview(request):
    if request.method=='POST':
            form=subsform(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('softname/')
    cat=request.POST['category']
    form=subsform()
    p=software_desc.objects.filter(category=cat)
    x=PageView.objects.all()[0]
    x.save()
    if p:
        return render(request,'personal/catview.html',{'q':p,'form':form,'page':x.hits})
    else:
        return render(request,'personal/catview.html',{'q':p,'form':form,'page':x.hits})


def softname(request):
    if request.method=='POST':
            form=subsform(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/')
    cat=request.POST['name']
    form=subsform()
    p=software_desc.objects.get(name=cat)
    p1=win_32.objects.filter(name=cat)
    p2=win_64.objects.filter(name=cat)
    p3=mac.objects.filter(name=cat)
    p4=android.objects.filter(name=cat)
    p5=request.user_agent.os.family
    x=PageView.objects.all()[0]
    x.save()
    if p:
        return render(request,'personal/detail.html',{'q':p,'q1':p1,'q2':p2,'q3':p3,'q4':p4,'form':form,'q5':p5,'page':x.hits})


def os(request):
    os = request.POST
    #print"name = ",softname.p
    #p=os.objects.get(name=cat)
    return HttpResponse("hello")


def search(request):
    squery = request.POST['search_box']
    form=subsform()
    x=PageView.objects.all()[0]
    x.save()
    if squery:
        s = software_desc.objects.filter(Q(name__icontains=squery)|Q(category__icontains=squery))
        if s:
            return render(request,'personal/catview.html',{'form':form,'q':s,'page':x.hits})
        else:
            return render(request,'personal/catview.html',{'form':form,'q':s,'page':x.hits})
