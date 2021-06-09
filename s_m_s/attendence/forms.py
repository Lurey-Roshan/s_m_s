from django import forms
from academic.models import ClassRegsitration


class SearchEnrolledStudentForm(forms.Form):
	reg_class=forms.ModelChoiceField(queryset=ClassRegsitration.objects.all())