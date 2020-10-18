# from __future__ import unicode_literals
# from django.db import models
# from django.contrib.auth.models import User
# from django.urls import reverse
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.db.models.signals import *
# from django.conf import settings

# # Create your models here.
# class subscribe(models.Model):
#     name=models.CharField(max_length=80)
#     email=models.CharField(max_length=80)

#     def __str__(self):
#         return '%s'%(self.email)




# class software_desc(models.Model):
#     pic=models.FileField(upload_to='media/',blank=True,null=True)
#     name=models.CharField(max_length=100,primary_key=True)
#     size=models.CharField(max_length=100)
#     version=models.CharField(max_length=100)
#     total_downloads=models.IntegerField()
#     ratings=models.CharField(max_length=20)
#     category=models.CharField(max_length=100)
#     desc=models.TextField()
#     def __str__(self):
#         return '%s'%(self.name)





# class win_32(models.Model):
#     name=models.ForeignKey(
#         software_desc,
#         on_delete=models.DO_NOTHING,
#     )
#     link=models.URLField()

#     def __str__(self):
#         return '%s'%(self.name)



# class win_64(models.Model):
#     name = models.ForeignKey(software_desc,
#                              on_delete=models.DO_NOTHING,)
#     link=models.URLField()

#     def __str__(self):
#         return '%s'%(self.name)



# class mac(models.Model):
#     name = models.ForeignKey(software_desc,
#                              on_delete=models.DO_NOTHING,)
#     link=models.URLField()

#     def __str__(self):
#         return '%s'%(self.name)


# class android(models.Model):
#     name = models.ForeignKey(software_desc,
#                              on_delete=models.DO_NOTHING,)
#     link=models.URLField()

#     def __str__(self):
#         return '%s'%(self.name)



# class feedback(models.Model):
#     name=models.CharField(max_length=30)
#     email=models.CharField(max_length=40)
#     comment=models.TextField(max_length=100)
# class post(models.Model):
#     title=models.CharField(max_length=40)
#     comment=models.TextField(max_length=100)
#     date_created=models.DateTimeField(auto_now=True,blank=True,null=True)
#     author = models.ForeignKey(
#         User, blank=True, null=True, on_delete=models.DO_NOTHING)
#     def __str__(self):
#         return '%s'%(self.title)
# class userex(models.Model):
#     user = models.OneToOneField(User, on_delete=models.DO_NOTHING,)
#     pic=models.FileField(upload_to='media/',blank=True,null=True)
#     def __str__(self):
#         return '%s'%(self.user)


# class PageView(models.Model):
#     hits=models.IntegerField(default=0)


from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class subscribe(models.Model):
    name = models.CharField(max_length=80)
    email = models.CharField(max_length=80)

    def __str__(self):
        return '%s' % (self.email)


class software_desc(models.Model):
    pic = models.FileField(upload_to='media/', blank=True, null=True)
    name = models.CharField(max_length=100, primary_key=True)
    size = models.CharField(max_length=100)
    version = models.CharField(max_length=100)
    total_downloads = models.IntegerField()
    ratings = models.CharField(max_length=20)
    category = models.CharField(max_length=100)
    desc = models.TextField()

    def __str__(self):
        return '%s' % (self.name)


class win_32(models.Model):
    name = models.ForeignKey(software_desc, on_delete=models.DO_NOTHING)
    link = models.URLField()

    def __str__(self):
        return '%s' % (self.name)


class win_64(models.Model):
    name = models.ForeignKey(software_desc, on_delete=models.DO_NOTHING)
    link = models.URLField()

    def __str__(self):
        return '%s' % (self.name)


class mac(models.Model):
    name = models.ForeignKey(software_desc, on_delete=models.DO_NOTHING)
    link = models.URLField()

    def __str__(self):
        return '%s' % (self.name)


class android(models.Model):
    name = models.ForeignKey(software_desc, on_delete=models.DO_NOTHING)
    link = models.URLField()

    def __str__(self):
        return '%s' % (self.name)


class feedback(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    comment = models.TextField(max_length=100)


class post(models.Model):
    title = models.CharField(max_length=40)
    comment = models.TextField(max_length=100)
    date_created = models.DateTimeField(auto_now=True, blank=True, null=True)
    author = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return '%s' % (self.title)


class userex(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    pic = models.FileField(upload_to='media/', blank=True, null=True)

    def __str__(self):
        return '%s' % (self.user)


class PageView(models.Model):
    hits = models.IntegerField(default=0)
