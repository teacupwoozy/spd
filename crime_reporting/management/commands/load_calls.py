import os
import csv
import logging
from datetime import datetime
from django.conf import settings
from crime_reporting.models import Call
from ast import literal_eval as make_tuple
from django.core.management.base import BaseCommand, CommandError

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Load police call data into the database."

    def flush_calls(self):
        """
        Wipe all the calls in the database.
        """
        Call.objects.all().delete()

    def parse_queued_timestamp(self, q):
        """
        Get a python timestamp object from the Arrived Time column in CSV
        """
        if q:
            parsed_queued_timestamp = datetime.strptime(
                q, "%m/%d/%Y %I:%M:%S %p")
            return parsed_queued_timestamp

    def parse_arrival_timestamp(self, t):
        """
        Get a python timestamp object from the Arrived Time column in CSV
        """
        if t:
            parsed_arrival_timestamp = datetime.strptime(t, "%b %d %Y %I:%M:%S:%f%p")
            return parsed_arrival_timestamp

    def get_is_sexual_assault(self, c):
        """
        If final call type is a kind of sexual assault, make true.
        """
        
        if "FAILURE" in c.final_call_type or "RACIAL" in c.final_call_type:
            return False
        elif "RAPE" in c.final_call_type or "SEX" in c.final_call_type:
            return True
        else:
            return False

    def handle(self, *args, **options):
        """
        Load in CSV of all police calls, creating Call objects.
        """
        self.data_dir = os.path.join(
            settings.ROOT_DIR, 'crime_reporting', 'data')
        # Delete all data in db:
        logger.debug("flushing calls")
        self.flush_calls()

        call_list = []

        # Source CSV
        paths = ['2018_Q1_All.csv']

        for p in paths:
            path = os.path.join(self.data_dir, p)
            reader = csv.DictReader(open(path, 'r'))
            for row in reader:
                c = Call(
                    cad_number = row["CAD Event Number"],
                    call_clearance_description = row[
                        "Event Clearance Description"],
                    method_call_received = row["Call Type"],
                    call_priority = row["Priority"],
                    initial_call_type = row["Initial Call Type"],
                    final_call_type = row["Final Call Type"],
                    # time_queued = row["Original Time Queued"],
                    # first_officer_arrival_time=row["Arrived Time"],
                    time_queued = self.parse_queued_timestamp(
                        row["Original Time Queued"]),
                    first_officer_arrival_time = self.parse_arrival_timestamp(
                        row["Arrived Time"]),
                    precinct = row["Precinct"],
                    sector = row["Sector"],
                    beat = row["Beat"]
                    )
                
                # Call back to methods on Call model
                c.is_sexual_assault = self.get_is_sexual_assault(c)

                call_list.append(c)

        # Batch upload calls to the database, 500 at a time
        Call.objects.bulk_create(
            call_list,
            batch_size=50
        )
