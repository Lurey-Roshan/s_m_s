from django.contrib import admin
from .models import StudentAttendence

# Register your models here.
class StudentAttendenceAdmin(admin.ModelAdmin):
	list_display=['class_name','student','date']

admin.site.register(StudentAttendence, StudentAttendenceAdmin)