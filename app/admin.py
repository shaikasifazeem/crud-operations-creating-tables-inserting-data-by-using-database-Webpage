from django.contrib import admin

# Register your models here.
from app.models import *
admin.site.register(College)
admin.site.register(Subjects)
admin.site.register(Student)
