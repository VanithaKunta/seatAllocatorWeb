from django.contrib import admin
from .models import classRooms,deptAndSec,addAndDel
# Register your models here.
admin.site.register(classRooms)
admin.site.register(deptAndSec)
admin.site.register(addAndDel)