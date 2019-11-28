from django.test import TestCase
from rest_framework.test import APIClient
from apps.lesson.models import Kanji
from apps.lesson.models import KanjiReadings


class KanjiOverviewTest(TestCase):

    def setUp(self):
        self.kanji = Kanji.objects.create(meaning='one', writing='一')
        self.kanji_reading = KanjiReadings.objects.create(reading_type='onyomi', reading='いち', kanji=self.kanji)

    def test_get_kanji_overview(self):
        client = APIClient()
        res = client.get('/api/kanji/')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data['total_kanji'], 1)
