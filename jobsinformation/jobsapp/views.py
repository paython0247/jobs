from django.shortcuts import render
from jobsapp.models import Hydjobs
from jobsapp.models import Punejobs
from jobsapp.models import Chennaijobs
from jobsapp.models import Banglorejobs
from jobsapp import forms
from jobsapp .models import Student
from django.contrib.auth.decorators import login_required
from jobsapp.forms import SignUpForm
from django.http import HttpResponseRedirect
# Create your views here.
def thankyou_view(request):
  return render(request,'thank.html')

def index(request):
	return render(request,'index.html')
@login_required
def hydjobs(request):
	hyd_list=Hydjobs.objects.all()
	my_dict={'hyd_list':hyd_list}
	return render(request,'hydjobs.html',context=my_dict)
@login_required
def punejobs(request):
	pune_list=Punejobs.objects.all()
	my_dict={'pune_list':pune_list}
	return render(request,'pune.html',context=my_dict)
def signup_view(request):
	form=SignUpForm()
	if request.method=='POST':
		form=SignUpForm(request.POST)
		user=form.save()
		user.set_password(user.password)
		user.save()
		return HttpResponseRedirect('/accounts/login')
	return render(request,'signup.html',{'form':form})




@login_required
def chennaijobs(request):
	chennai_list=Chennaijobs.objects.all()
	my_dict={'chennai_list':chennai_list}
	return render(request,'chennai.html',context=my_dict)

@login_required
def banglorejobs(request):
	banglore_list=Banglorejobs.objects.all()
	my_dict={'banglore_list':banglore_list}
	return render(request,'banglore.html',context=my_dict)



@login_required
def banglorejobs(request):
	banglore_list=Banglorejobs.objects.all()
	my_dict={'banglore_list':banglore_list}
	return render(request,'banglore.html',context=my_dict)



@login_required
def student_view(request):
	form=forms.StudentForm()
	if request.method=='POST':
		form=forms.StudentForm(request.POST)
		if form.is_valid():
			form.save(commit=True)
			return thankyou_view(request)
	
	return render(request ,'form.html',{'form':form})


@login_required
def list_student(request):
	student_list=Student.objects.all()
	return render(request,'student.html',{'student_list':student_list})
