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
from django.urls import reverse
from django.contrib.auth.models import User
from home.models import userex
from home.models import post
from django.shortcuts import render
from .forms import Regforms
from django.views.generic import CreateView
from django import forms
# from django_user_agents.utils import get_user_agent
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

#from django.core.context_processors import csrf
# Create your views here.
def index(request):
    p=post.objects.order_by('-date_created')
    f=request.user
    if request.method=='POST':
        forms=homeform(request.POST)
        if forms.is_valid():
            f=forms.save(commit=False)
            f.author=request.user
            f.save()
            return HttpResponseRedirect('/community/')
    else:
        forms=homeform()
    return render(request,'home.html',{'form':forms,'q':p,'cu':f})

def login(request):
    p=post.objects.order_by('-date_created')
    return render(request,'login.html',{'q':p})
    
def delete(request,d):
    m=post.objects.get(id=d)
    m.delete()
    return HttpResponseRedirect('/community/')

def register(request):
    user=request.user
    if request.method=='POST':
        form=Regforms(request.POST,request.FILES)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            #confirm_password=form.cleaned_data['confirm_password']
            email=form.cleaned_data['email']
            #pic=form.cleaned_data['pic']

            user=User.objects.create_user(username=username, password=password,
                                     email=email,first_name=first_name,last_name=last_name)

            f=form.save(commit=False)
            f.user=user
            f.save()
            return HttpResponseRedirect('/community/')
            #return render(request,'login.html')
    else:
        '''form=Regforms(instance=User,
                      intial={'pic':pic})'''
        form=Regforms()
    return render(request,'register.html',{'form':form})

def edit(request, d):
    user= request.user
    m=User.objects.get(id=d)
    if request.method=='POST':
        form=Editforms(request.POST,request.FILES,instance = m)
        user=User.objects.filter(id=d)
        if form.is_valid():
            password=form.cleaned_data['password']
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            email=form.cleaned_data['email']
            #confirm_password=form.cleaned_data['confirm_password']
            pic=form.cleaned_data['pic']
            user=form.save()
            #user.update(first_name=first_name,last_name=last_name,email=email)

            u=userex.objects.filter(user_id=d)
            u.delete()
            f=form.save(commit=False)
            f.user=user
            f.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return HttpResponseRedirect('/community/')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form=Editforms(instance = m)
    return render(request,'register.html',{'form':form})




def home(request):
    if request.user.is_authenticated:
        return index(request)
    else:
        return login(request)

def auth_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username,password=password)
    if user is not None:
        auth.login(request,user)
        return HttpResponseRedirect('/community/')
    else:
        return render(request,'invalid.html')
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/community/')
#try:
#    match=User.objects.get(email=umail)
#except:
#    return self.cleaned_data['email']
#raise forms.ValidationError('email already registered..!!')
def search(request):
    f=request.user
    squery = request.GET['search_box']
    forms=homeform()
    if squery:
        s = post.objects.filter(Q(title__icontains=squery)|Q(comment__icontains=squery)|Q(author__username__icontains=squery))
        if s:
            return render(request,'home.html',{'form':forms,'q':s,'cu':f})
        else:
            #return HttpResponse('Sorry No Reuslts Found..!')
            return render(request,'home.html',{'form':forms,'q':s,'cu':f})

    else:
        return HttpResponseRedirect('/')

def update(request,d):
    p=post.objects.order_by('-date_created')
    f=request.user
    m=post.objects.get(id=d)
    if request.method=='POST':
        form=homeform(request.POST,instance = m)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/community/')
    else:
        form=homeform(instance = m)
    return render(request,'home.html',{'form':form,'cu':f,'q':p})


def listing(request):
    contact_list = post.objects.all()
    paginator = Paginator(contact_list, 3) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)

    return render(request, 'home.html', {'contacts': contacts})
