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
        context['is_lewd_conduct'] = calls.filter(
            final_call_type='--SEX OFFENSES (NON-RAPE) - LEWD CONDUCT')
        # Count of is_lewd_conduct
        context['is_lewd_conduct_count'] = context['is_lewd_conduct'].count()

        # Calls reporting molesting
        context['is_molesting'] = calls.filter(
            final_call_type='--SEX OFFENSES (RAPE) - MOLESTING')
        # Count of is_molesting
        context['is_molesting_count'] = context['is_molesting'].count()

        # Calls reporting commercial sexual exploitation of minors (CSEC)
        context['is_CSEC'] = calls.filter(
            final_call_type='--COMMERCIAL SEXUAL EXPLOITATION OF MINORS (CSEC)')
        # Count of is_CSEC
        context['is_CSEC_count'] = context['is_CSEC'].count()

        # Calls reporting rape
        context['is_rape_call_type'] = calls.filter(
            final_call_type='RAPE')
        # Count of is_rape
        context['is_rape_call_type_count'] = context['is_rape_call_type'].count()

        # Calls reporting an in-progress or just-occurred rape
        context['is_ip_jo_rape'] = calls.filter(
            final_call_type='RAPE - IP/JO')
        # Count of ip_or_jo_rape
        context['is_ip_jo_rape_count'] = context['is_ip_jo_rape'].count()

        # Calls reporting an aquaintance rape
        context['is_aquaintance_rape'] = calls.filter(
            final_call_type='--RAPE - KNOWN SUSPECT (ACQUAINTANCE)')
        # Count of is_aquaintance_rape
        context['is_aquaintance_rape_count'] = context['is_aquaintance_rape'].count()

        # Calls reporting a stranger rape
        context['is_stranger_rape'] = calls.filter(
            final_call_type='--RAPE - UNKNOWN SUSPECT (STRANGER)')
        # Count of is_stranger_rape
        context['is_stranger_rape_count'] = context['is_stranger_rape'].count()

        # Count of all_rapes
        # all_rapes = [
        #     context['is_rape'], 
        #     context['is_rape_count'],
        #     ]
        # context['total_all_rapes'] = calls.Sum('all_rapes')


        context['is_rape'] = calls.filter(is_rape=True)
        # Count of is_rape
        context['is_rape_count'] = context['is_rape'].count()



        return context


