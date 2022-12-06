from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# home 핸들러
def home(request):

    return HttpResponse("THIS IS HOMEPAGE!!")