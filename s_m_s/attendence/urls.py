from django.urls import path
from .viiews import student_attendence, SetAttendence

urlpatterns=[
	path('student/',student_attendence ,name='student-attendence'),
	path('set-attendence/<std_class>/<std_roll>', SetAttendence.as_view(), name='set-attendence')
]