from rest_framework import serializers
from .models import Kanji
from .models import KanjiReadings


class KanjiReadingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = KanjiReadings
        fields = ['reading_type', 'reading']


class KanjiSerializer(serializers.ModelSerializer):
    readings = KanjiReadingsSerializer(many=True)

    class Meta:
        model = Kanji
        fields = ['writing', 'meaning', 'readings']
