from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from meddata.models import Drug

def index(request):
	return render(request, 'meddata/index.html')