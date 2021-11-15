from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from website1.forms import SignUpForm
from django.http import HttpResponseRedirect

# Create your views here.
def home_page_view(request):
	return render(request,'website1/home.html')

@login_required
def java_exams_view(request):
	return render(request,'website1/javaexams.html')

@login_required
def python_exams_view(request):
	return render(request,'website1/pythonexams.html')

@login_required
def aptitude_exams_view(request):
	return render(request,'website1/aptitudeexams.html')

def logout_view(request):
	return render(request,'website1/logout.html')

def signup_view(request):
	form=SignUpForm()
	if request.method=='POST':
		form=SignUpForm(request.POST)
		if form.is_valid():
			user=form.save()
			user.set_password(user.password)
			user.save()
			return HttpResponseRedirect('/accounts/login')
	return render(request,'website1/signup.html',{'form':form})
