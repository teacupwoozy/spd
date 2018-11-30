import os
import csv
import logging
from datetime import datetime
from django.conf import settings
from crime_reporting.models import Call
from ast import literal_eval as make_tuple
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Load police call data into the database."

    def handle(self, *args, **options):
        """
        Load in CSV of all police calls, creating Call objects.
        """
