from django.db import models
from . import constants


class Kana(models.Model):
    writing = models.CharField(max_length=25, blank=False, unique=True)
    kana_type = models.CharField(choices=constants.KANA_TYPE_CHOICES, max_length=10)

    class Meta:
        app_label = 'lesson'


class Kanji(models.Model):
    writing = models.CharField(max_length=25, blank=False, unique=True)
    meaning = models.CharField(max_length=100, blank=False)
    level = models.PositiveIntegerField(blank=False, default=1)
    important_reading = models.CharField(choices=constants.KANJI_READING_CHOICES, max_length=10, default=constants.ONYOMI)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'lesson'


class KanjiReadings(models.Model):
    kanji = models.ForeignKey(Kanji, related_name='readings', on_delete=models.CASCADE)
    reading_type = models.CharField(choices=constants.KANJI_READING_CHOICES, max_length=10, default=constants.ONYOMI)
    reading = models.CharField(max_length=25, blank=False)

    class Meta:
        app_label = 'lesson'


class Vocabulary(models.Model):
    writing = models.CharField(max_length=25, blank=False, unique=True)
    kana = models.CharField(max_length=25, blank=False)
    meaning = models.CharField(max_length=100, blank=False)
    level = models.PositiveIntegerField(blank=False, default=1)

    class Meta:
        app_label = 'lesson'
