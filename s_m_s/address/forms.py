from django import forms
from . models import *

class DistrictForm(forms.ModelForm):
	class meta:
		model=District
		fields='__all__'
		widgets={
		'name':forms.TextInput(attrs={'class':'form-control'})
		}

class UpazillaForm(forms.ModelForm):
	class meta:
		model=Upazilla
		fields='__all__'
		widgets={
			'district':forms.Select(attrs={'class':'form-control'}),
			'name':forms.TextInput(attrs={'class':'form-control'}),
		}

class UnionForm(forms.ModelForm):
	class meta:
		model=Union
		fields='__all__'
		widgets={
			'district':forms.Select(attrs={'class':'form-control'}),
			'upazilla':forms.Select(attrs={'class':'form-control'}),
			'name':forms.TextInput(attrs={'class':'form-control'}),

		}
		