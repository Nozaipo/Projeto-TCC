from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def get_risks(request):
	if request.method == 'POST':
		risks = []
		risks = request.POST.getlist("risks")
		print(risks)

def checklist(request):
	all_risks = Risk.objects.filter(active=1)
	return render(request, 'checklist.html', {'risks': all_risks})

def form_history(request):
	all_forms = Form.objects.all()
	return render(request, 'form_history.html', {'forms': all_forms})

def clear(request):
	Form.objects.all().delete()
	return HttpResponseRedirect('/')

@login_required
def save_record(request):
	print(request.POST.getlist('risk'))
	risk_observed = Risk.objects.filter(risk_name__in=request.POST.getlist('risk'))
	print(risk_observed)
	new_form = Form()
	new_form.who_applied = request.user.get_full_name()
	new_form.save()
	new_form.risks_observed.add(*risk_observed)
	new_form.save()

	# form.risks_observed.add(*risk_observed)
	
	# form.save()

	return HttpResponseRedirect('/')

def web_login(request):
	if request.method == 'GET':
		return render(request, 'login.html')
	else:
		user = request.POST.get('uname')
		password = request.POST.get('psw')
		user = authenticate(username=user, password=password)

		if user:
			login(request, user)
			return render(request, 'checklist.html')
		return HttpResponse("Falha ao logar.")

@login_required
def web_logout(request):
	logout(request)
	return render(request, 'login.html')
	
def check_user(request):
	print(request.user.get_full_name())
	return HttpResponse(request.user)