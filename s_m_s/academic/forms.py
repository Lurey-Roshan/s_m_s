from django import forms
from academic.models import Department,  ClassInfo, ClassRegistration, Shift, Session, Section, GuideTeacher


class DepartmentForm(forms.ModelForm):
	class meta:
		model=models.Department
		fields='__all__'
		widgets={
			'name':forms.TextInput(attrs={'class':'form-control'}),
		}

class ClassInfoForm(forms.ModelForm):
	class meta:
		model=models.ClassInfo
		fields='__all__'
		widgets={
			'name':forms.TextInput(attrs={'class':'form-control'}),
			'display_name':forms.TextInput(attrs={'class':'form-control'}),

		}

class ShiftForm(forms.ModelForm):
	class meta:
		model=models.Shift
		fields='__all__'
		widgets={
			'name':forms.TextInput(attrs={'class':'form-control'}),
		}
class SessionForm(forms.ModelForm):
	class meta:
		model=models.Session
		fields='__all__'
		widgets={
			'name':forms.TextInput(attrs={'class':'form-control'}),
		}
class SectionForm(forms.ModelForm):
	class meta:
		model=models.Section
		fields='__all__'
		widgets={
			'name':forms.TextInput(attrs={'class':'form-control'}),
		}
class ClassRegistrationForm(forms.ModelForm):
	class meta:
		model=models.ClassRegistration
		fields='__all__'
		widgets={
			'name':forms.TextInput(attrs={'class':'form-control'}),
			'department':forms.TextInput(attrs={'class':'form-control'}),
			'class_name':forms.TextInput(attrs={'class':'form-control'}),
			'section':forms.TextInput(attrs={'class':'form-control'}),
			'session':forms.TextInput(attrs={'class':'form-control'}),
			'shift':forms.TextInput(attrs={'class':'form-control'}),
			'guide_teacher':forms.TextInput(attrs={'class':'form-control'}),
		}
class GuideTeacherForm(forms.ModelForm):
	class meta:
		model=models.GuideTeacher
		fields='__all__'
		widgets={
			'name':forms.TextInput(attrs={'class':'form-control'}),
		}
