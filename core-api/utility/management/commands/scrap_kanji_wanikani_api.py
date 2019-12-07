import requests

from django.core.management.base import BaseCommand, CommandError
from apps.lesson import constants
from apps.lesson.models import Kanji
from apps.lesson.models import KanjiReadings


K_WANIKANI_API_ENDPOINT = 'https://www.wanikani.com/api/user/fb45af3089485d735f117bc954f27bb2'

class Command(BaseCommand):
    help = 'Scrap kanji from wanikani APIs'

    def add_arguments(self, parser):
        parser.add_argument('levels', nargs='+', type=int)

    def handle(self, *args, **options):
        for level in options['levels']:
            url = '{}/kanji/{}'.format(K_WANIKANI_API_ENDPOINT, level)
            r = requests.get(url)
            result = r.json()
            for kanji_data in result['requested_information']:
                writing = kanji_data['character']
                meaning = kanji_data['meaning']
                onyomi = kanji_data['onyomi']
                kunyomi = kanji_data['kunyomi']
                important_reading = kanji_data['important_reading']
                kanji, _ = Kanji.objects.get_or_create(writing=writing, meaning=meaning, level=level, important_reading=important_reading)
                if onyomi:
                    onyomi_reading = KanjiReadings.objects.get_or_create(kanji=kanji, reading_type=constants.ONYOMI, reading=onyomi)
                if kunyomi:
                    kunyomi_reading = KanjiReadings.objects.get_or_create(kanji=kanji, reading_type=constants.KUNYOMI, reading=kunyomi)
