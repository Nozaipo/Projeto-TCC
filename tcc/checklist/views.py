from django.shortcuts import render
from django.http import HttpResponse
from .models import Risk

# Create your views here.


def get_risks(request):
	if request.method == 'POST':
		risks = []
		risks = request.POST.getlist("risks")
		print(risks)

def checklist(request):
	all_risks = Risk.objects.filter(active=1)
	return render(request, 'checklist.html', {'risks': all_risks})

def risks_observed(request):
	print(request.POST.getlist('risk'))
	return HttpResponse('teste')