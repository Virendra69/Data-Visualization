# management/commands/read_json_to_db.py
import json
from datetime import datetime
from django.core.management.base import BaseCommand
from App.models import Data  # Import your model


def convertDate(timestamp_str):
    print(timestamp_str)
    if timestamp_str:
        # Convert string to datetime object
        timestamp = datetime.strptime(timestamp_str, "%B, %d %Y %H:%M:%S")

        # Format datetime object
        return timestamp.strftime("%Y-%m-%d %H:%M:%S")
    else:
        return "1970-01-01 00:00:00"


class Command(BaseCommand):
    help = 'Reads JSON file and saves data to the database'

    def handle(self, *args, **options):
        with open('jsondata.json', 'r', encoding='utf-8') as file:
            json_data = json.load(file)

        for data in json_data:

            data = Data(
                end_year=data['end_year'],
                intensity=data['intensity'],
                sector=data['sector'],
                topic=data['topic'],
                insight=data['insight'],
                url=data['url'],
                region=data['region'],
                start_year=data['start_year'],
                impact=data['impact'],
                added=convertDate(data['added']),
                published=convertDate(data['published']),
                country=data['country'],
                relevance=data['relevance'],
                pestle=data['pestle'],
                source=data['source'],
                title=data['title'],
                likelihood=data['likelihood']
            )
            data.save()

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
