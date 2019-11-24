from django.db import models


class Kanji(models.Model):
    writing = models.CharField(max_length=25, blank=False, unique=True)
    meaning = models.CharField(max_length=50, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'kanji'


class KanjiReadings(models.Model):
    KUNYOMI = 'kunyomi'
    ONYOMI = 'onyomi'

    KANJI_READING_CHOICES = [
        (KUNYOMI, "kun'yomi"),
        (ONYOMI, "on'yomi")
    ]

    kanji = models.ForeignKey(Kanji, related_name='readings', on_delete=models.CASCADE)
    reading_type = models.CharField(choices=KANJI_READING_CHOICES, max_length=10, default=ONYOMI)
    reading = models.CharField(max_length=25, blank=False)

    class Meta:
        app_label = 'kanji'
