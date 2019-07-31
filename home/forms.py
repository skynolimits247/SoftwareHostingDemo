from __future__ import unicode_literals
from django import forms
from .models import *
from .views import *
from django.db import models


class subsform(forms.ModelForm):
    name=forms.CharField(widget=forms.TextInput
                         (attrs={'class':'panel','length':'100'}),
                         label="Enter you Name",
                         max_length=80,
                         required=True)
    email=forms.CharField(widget=forms.EmailInput
                          (attrs={'class':'panel','length':'100'}),
                          label="Enter your Email",
                          max_length=80,
                          required=True)
    def clean_email(self):
        umail=self.cleaned_data['email']
        try:
            match=subscribe.objects.get(email=umail)
        except:
            return self.cleaned_data['email']
        raise forms.ValidationError('email already registered..!!')
    class Meta:
        model=subscribe
        fields=['name','email']
