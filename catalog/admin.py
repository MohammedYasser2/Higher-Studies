from atexit import register
from django.contrib import admin

# Register your models here.
from .models import Students,Courses


# Register your models here.

admin.site.register(Students)
admin.site.register(Courses)
