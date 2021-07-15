
	#def starts_with_s(value):
	#	if value[0]!='s':
	 #   	    raise forms.ValidationError('Name Should start with s')

      





from django import forms
from jobsapp .models import Student
class StudentForm(forms.ModelForm):
	class Meta:
		model=Student
		fields='name','marks','add','mobile','email'
		
from django.contrib.auth.models import User
class SignUpForm(forms.ModelForm):
	class Meta:
		model=User
		fields=['username','password','email','first_name','last_name']



	











