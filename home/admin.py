from __future__ import unicode_literals

from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(subscribe)
admin.site.register(software_desc)
admin.site.register(win_32)
admin.site.register(win_64)
admin.site.register(mac)
admin.site.register(android)
admin.site.register(feedback)
