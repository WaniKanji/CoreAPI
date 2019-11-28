import requests

from django.core.management.base import BaseCommand, CommandError
from apps.kanji import constants
from apps.kanji.models import Kanji
from apps.kanji.models import KanjiReadings


K_WANIKANI_API_ENDPOINT = 'https://www.wanikani.com/api/user/0366768dc874416f4257f4e0486de9a4'
K_WANIKANI_MAX_LEVEL = 60

class Command(BaseCommand):
    help = 'Scrap kanji from wanikani APIs'

    def handle(self, *args, **options):
        for level in range(1, K_WANIKANI_MAX_LEVEL + 1):
            url = '{}/kanji/{}'.format(K_WANIKANI_API_ENDPOINT, level)
            r = requests.get(url)
            result = r.json()
            for kanji in result['requested_information']:
                writing = kanji['character']
                meaning = kanji['meaning']
                onyomi = kanji['onyomi']
                kunyomi = kanji['kunyomi']
                important_reading = kanji['important_reading']
                kanji, _ = Kanji.objects.get_or_create(writing=writing, meaning=meaning, level=level, important_reading=important_reading)
                if onyomi:
                    onyomi_reading = KanjiReadings.objects.get_or_create(kanji=kanji, reading_type=constants.ONYOMI, reading=onyomi)
                if kunyomi:
                    kunyomi_reading = KanjiReadings.objects.get_or_create(kanji=kanji, reading_type=constants.KUNYOMI, reading=kunyomi)
