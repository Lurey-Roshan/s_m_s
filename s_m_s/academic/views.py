from django.shortcuts import render, redirect
from academic.forms import *
from academic.models import *

# Create your views here.
def add_department(request):
	forms=DepartmentForm()
	if request.method=='POSt':
		forms=DepartmentForm(request.POST)
		if forms.is_valid():
			forms.save()
			return redirect('add-department')
	department=Department.objects.all()
	context={'forms':forms,'departmemt':department}
	return render(request,'academic/add-department.html')

def add_class(request):
	forms=ClassForm()
	if request.method=='POST':
		forms=ClassForm(request.POST)
		if forms.is_valid():
			forms.save()
			return redirect('create-class')
	class_obj=ClassInfo.objects.all()
	context={
		'forms':forms,
		'class_obj':class_obj
	}
	retun render(request, 'academic/create-class.html')

def create_section(request):
	forms=SectionForm()
	if request.method=='POST':
		forms=SectionForm(request.POST)
		if forms.is_valid():
			forms.save()
			return redirect('create-section')
	section=Section.objects.all()
	context={
		'forms':forms, 'section':section
	}
	return render(request, 'academic/create-section.html')

def create_session(request):
	forms=SessionForm()
	if request.method=='POST':
		forms=SessionForm(request.POST)
		if forms.is_valid():
			forms.save()
			return redirect('create-session')
	session=Session.objects.all()
	context={'forms':forms,'session':session}
	return render(request, 'academic/create-session.html')

def create_shift(request):
	forms=ShiftForm()
	if request.method=='POST':
		forms=ShiftForm(request.POST)
		if forms.is_valid():
			forms.save()
			return redirect('create-shift')
	shitf=Shift.objects.all()
	context={
		'forms':forms, 'shift':shitf
	}
	return render(request,'academic/create-shift.html')

def class_registration(request):
	forms=ClassRegistrationForm()
	if request.method =='POST':
		forms=ClassRegistrationForm(request.POST)
		if forms.is_valid():
			forms.save()
			return redirect('class-list')
	context={'forms':forms}
	return render(request,'academic/class-registration.html')

def class_list(request):
	register_class=ClassRegistration.objects.all()
	context={'register_class':register_class}
	return render(request,'academic/class-list.html')

def create_guide_teacher(request):
	forms=GuideTeacherForm()
	if request.method=='POST':
		forms=GuideTeacherForm(request.POST)
		if forms.is_valid():
			forms.save()
			return redirect('guide-teacher')
	guide_teacher=GuideTeacher.objects.all()
	context={'forms':forms, 'guide_teacher':guide_teacher}
	return render(request, 'academic/create-guide-teacher.html')