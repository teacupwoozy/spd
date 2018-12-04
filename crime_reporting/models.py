import logging
# import calculate
from datetime import datetime
from django.conf import settings
from django.db import models
from django.db.models import Avg
from django.utils import dateformat

logger = logging.getLogger(__name__)

# Create your models here.


class Call(models.Model):
    """
    A list of police calls made to Seattle Police Department
    """
    cad_number = models.IntegerField(db_index=True, help_text='CAD event number')
    call_clearance_description = models.CharField(max_length=100, blank=True, null=True)
    method_call_received = models.CharField(max_length=80, blank=True, null=True)
    call_priority = models.IntegerField(default=0)
    initial_call_type = models.CharField(max_length=120, blank=True, null=True)
    final_call_type = models.CharField(max_length=120, blank=True, null=True)
    time_queued = models.DateTimeField(blank=True, null=True)
    first_officer_arrival_time = models.DateTimeField(blank=True, null=True)
    precinct = models.CharField(max_length=20, blank=True, null=True)
    sector = models.CharField(max_length=20, blank=True, null=True)
    beat = models.CharField(max_length=3, blank=True, null=True)

    # Add add-on columns
    # Is crime a sexual assault, default value is False
    is_sexual_assault = models.BooleanField()
    # Is crime a rape, default value is False
    is_rape = models.BooleanField()
    
    # Managers
    objects = models.Manager()

    class Meta:
        ordering = ("-time_queued",)

    def __str__(self):
        return self.cad_number
