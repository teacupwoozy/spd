from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Call
from django.views.generic.base import TemplateView

# Create your views here.


def index(request):
    return HttpResponse("Hallo. This is the Crime Reporting index page.")

# def call_analysis(request):
#     return render(request, 'crime_reporting/call_analysis.html')


class CallAnalysis(TemplateView):
    # The HTML template
    template_name = "crime_reporting/call_analysis.html"

    # def __init__(self):


    def get_context_data(self, **kwargs):
        # Access all calls
        calls = Call.objects.all()
        
        context = super(CallAnalysis, self).get_context_data(**kwargs)
        context['title'] = "Hallo. Call Analysis page"
        # Calls that are reporting a sexual assault
        context['is_sexual_assault'] = calls.filter(is_sexual_assault=True)
        # Count of is_sexual_assault
        context['is_sexual_assault_count'] = context['is_sexual_assault'].count()
        return context


