from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import response
from rest_framework import status

from .forms import SearchEnrolledStudentForm
from student.models import EnrolledStudent
from academic.models import ClassRegistration
from .models import StudentAttendence
# Create your views here.
def student_attendence(request):
	forms=SearchEnrolledStudentForm()
	class_name=request.Get.get('reg_class', None)
	if class_name:
		class_info=ClassRegistration.objects.get(id=class_name)
		student=EnrolledStudent.objects.filter(class_name=class_name)
		context={
			'forms':forms,
			'student':student,
			'class_info':class_info
		}
		return render(request, 'attendence/student-attendence.html')
	context={'forms':forms}
	return render(request,'attendence/student-attendence.html', context)

 class SetAttendence(APIView):
 	def get(self, request,std_class, std_roll):
 		try:
 			StudentAttendence.objects.create_attendence(std_class, std_roll)
 			return Response({'status':'Success'}, status=status.HTTP_200_OK)
 		except:
 			return Response({'status':'Failed'},status=status.HTTP_400_BAD_REQUEST)
 			
