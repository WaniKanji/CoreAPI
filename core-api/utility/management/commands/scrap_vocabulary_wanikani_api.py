import requests

from django.core.management.base import BaseCommand, CommandError
from apps.lesson import constants
from apps.lesson.models import Vocabulary


K_WANIKANI_API_ENDPOINT = 'https://www.wanikani.com/api/user/0366768dc874416f4257f4e0486de9a4'

class Command(BaseCommand):
    help = 'Scrap kanji from wanikani APIs'

    def add_arguments(self, parser):
        parser.add_argument('levels', nargs='+', type=int)

    def handle(self, *args, **options):
        for level in options['levels']:
            url = '{}/vocabulary/{}'.format(K_WANIKANI_API_ENDPOINT, level)
            r = requests.get(url)
            result = r.json()
            for vocabulary_data in result['requested_information']:
                writing = vocabulary_data['character']
                meaning = vocabulary_data['meaning']
                kana = vocabulary_data['kana']
                vocabulary, _ = Vocabulary.objects.get_or_create(writing=writing, kana=kana, meaning=meaning, level=level)
