from django.shortcuts import render , redirect
from . import forms
from .models import PersonalInfo

# Create your views here.
from address.models import District, Upazilla, Union

def load_upazilla(request):
	district_id=request.Get.get('district')
	upazilla=Upazilla.objects.filter(district_id=district_id).order_by('name')
	upazilla_id=request.Get.get('upazilla')
	union=Union.objects.filter(upazilla_id=upazilla_id).order_by('name')
	context={
		'upazilla':upazilla,
		'union':union
	}
	return render(request,'others/upazilla_dropdown_list_options.html', context)

def teacher_registration(request):
	forms=forms.PersonalInfoForm()
	address_forms=forms.AddressInfoForm()
	education_forms=forms.EducationInfoForm()
	training_forms=forms.TrainingInfoForm()
	job_forms=forms.JobInfoForm()
	experience_forms=forms.ExperienceInfoForm()
	if request.method=='POST':
		forms=forms.PersonalInfoForm(request.POST)
		address_forms=forms.AddressInfoForm(request.POST)
		education_forms=forms.EducationInfoForm(request.POST)
		training_forms=forms.TrainingInfoForm(request.POST)
		job_forms=forms.JobInfoForm(request.POST)
		experience_forms=forms.ExperienceInfoForm(request.POST)
		if forms.is_valid() and address_forms.is_valid() and education_forms.is_valid() and training_forms.is_valid() and job_forms.is_valid() and experience_forms.is_valid():
			personal_info=forms.save()
			address_info=address_forms.save(commit=False)
			address_info.address= personal_info
			address_info.save()
			education_info=education_forms.save(commit=False)
			education_info.education=personal_info
			education_info.save()
			training_info=training_forms.save(commit=False)
			training_info.training=personal_info
			training_info.save()
			job_info=job_forms.save(commit=False)
			job_forms.Job=personal_info
			job_forms.save()
			experience_info=experience_forms.save(commit=False)
			experience_forms.experence=personal_info
			experience_forms.save()
			return redirect('employee-list')

	context={
		'forms':forms,
		'address_forms':address_forms,
		'education_forms':education_forms,
		'training_forms':training_forms,
		'job_forms':job_forms,
		'experience_forms':experience_forms
	}
	return render(request, 'employee/employee-registration.html', context)

def teacher_list(request):
	teacher=PersonalInfo.objects.all()
	context={'teacher':teacher}
	return render(request, 'employee/employee-list.html', context)