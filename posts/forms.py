from __future__ import unicode_literals
from django.test import TestCase
# Create your tests here.
from django import forms
from .models import *
from .views import *
from django.db import models
from django.contrib.auth.models import User
from home.models import userex
from home.models import post
from django.contrib.auth.models import AbstractUser
from home.models import *

class Editforms(forms.ModelForm):
    username=forms.CharField(widget=forms.TextInput
                             (attrs={'class':'form-control'}),
                             label="Enter your User Name",
                             max_length=30,
                             required=True)
    first_name=forms.CharField(widget=forms.TextInput
                                 (attrs={'class':'form-control'}),
                                 label="Enter your First Name",
                                 max_length=30,
                                 required=True)

    last_name=forms.CharField(widget=forms.TextInput
                                 (attrs={'class':'form-control'}),
                                 label="Enter your Last Name",
                                 max_length=30,
                                 required=True)

    email=forms.CharField(widget=forms.EmailInput
                          (attrs={'class':'form-control'}),
                          label="Enter your Email",
                          max_length=30,
                          required=True)
    password=forms.CharField(widget=forms.PasswordInput
                             (attrs={'class':'form-control'}),
                             label="Type your password",
                             max_length=30,
                             required=True)
    confirm_password=forms.CharField(widget=forms.PasswordInput
                             (attrs={'class':'form-control'}),
                            label="Confirm your password",
                             max_length=30,
                             required=True)
    pic=forms.FileField()

    def clean_confirm_password(self):
        print"pass check"
        print "i= pass_",self.cleaned_data
        pas=self.cleaned_data['password']
        conpass=self.cleaned_data['confirm_password']
        print "i= conpass_",self.cleaned_data['confirm_password']
        if pas != conpass:
            raise forms.ValidationError('password and confirm password do not match')

    def clean_email(self):
        uname=self.cleaned_data['username']
        print"email check"
        umail=self.cleaned_data['email']
        try:
            match=User.objects.get(email=umail).filter(username != uname)
        except:
            return self.cleaned_data['email']
        raise forms.ValidationError('email already registered..!!')


    class Meta:
        model=userex
        fields=['username','first_name','last_name','password','confirm_password','email','pic']
# Create your models here.

class Regforms(forms.ModelForm):
    username=forms.CharField(widget=forms.TextInput
                             (attrs={'class':'form-control'}),
                             label="Enter your User Name",
                             max_length=30,
                             required=True)
    first_name=forms.CharField(widget=forms.TextInput
                                 (attrs={'class':'form-control'}),
                                 label="Enter your First Name",
                                 max_length=30,
                                 required=True)

    last_name=forms.CharField(widget=forms.TextInput
                                 (attrs={'class':'form-control'}),
                                 label="Enter your Last Name",
                                 max_length=30,
                                 required=True)

    email=forms.CharField(widget=forms.EmailInput
                          (attrs={'class':'form-control'}),
                          label="Enter your Email",
                          max_length=30,
                          required=True)
    password=forms.CharField(widget=forms.PasswordInput
                             (attrs={'class':'form-control'}),
                             label="Type your password",
                             max_length=30,
                             required=True)
    confirm_password=forms.CharField(widget=forms.PasswordInput
                             (attrs={'class':'form-control'}),
                            label="Confirm your password",
                             max_length=30,
                             required=True)
    pic=forms.FileField()

    def clean_username(self):
        print"uid check slf.cleaned data",self.cleaned_data
        uname=self.cleaned_data['username']
        try:
            match=User.objects.get(username=uname)
        except:
            return self.cleaned_data['username']
        raise forms.ValidationError('Username already exists..!!')
    def clean_confirm_password(self):
        print"pass check"
        print "i= pass_",self.cleaned_data
        pas=self.cleaned_data['password']
        conpass=self.cleaned_data['confirm_password']
        print "i= conpass_",self.cleaned_data['confirm_password']
        if pas != conpass:
            raise forms.ValidationError('password and confirm password do not match')

    def clean_email(self):
        print"email check"
        umail=self.cleaned_data['email']
        try:
            match=User.objects.get(email=umail)
        except:
            return self.cleaned_data['email']
        raise forms.ValidationError('email already registered..!!')


    class Meta:
        model=userex
        fields=['username','first_name','last_name','password','confirm_password','email','pic']

class homeform(forms.ModelForm):
    class Meta:
        model=post
        fields= ['title','comment']
