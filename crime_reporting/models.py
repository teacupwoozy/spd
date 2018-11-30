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
