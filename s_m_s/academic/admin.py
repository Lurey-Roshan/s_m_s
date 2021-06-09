from django.contrib import admin

# Register your models here.
from academic.models import Department, ClassInfo, ClassRegistration, Shift, Session, Section, GuideTeacher

admin.site.register(Department)
admin.site.register(ClassInfo)
admin.site.register(Section)
admin.site.register(Shift)
admin.site.register(Session)
admin.site.register(ClassRegistration)
admin.site.register(GuideTeacher)