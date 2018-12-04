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

        # Calls reporting lewd conduct
        # Count of is_lewd_conduct

        # Calls reporting molesting
        # Count of is_molesting

        # Calls reporting commercial sexual exploitation of minors (CSEC)
        # Count of is_CSEC

        # Calls reporting rape
        # Count of is_rape

        # Calls reporting an in-progress or just-occurred rape
        # Count of ip_or_jo_rape

        # Calls reporting an aquaintance rape
        # Count of is_aquaintance_rape

        # Calls reporting a stranger rape
        # Count of is_stranger_rape

        # Count of all_rapes

        return context


