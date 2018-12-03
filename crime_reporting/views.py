from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Hallo. This is the Crime Reporting index page.")

def call_analysis(request):
    # return render(request, 'crime_reporting/templates/call_analysis.html', {})
    return HttpResponse("Call analysis page")
