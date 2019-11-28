from django.shortcuts import render
from rest_framework import views
from rest_framework import response
from rest_framework import generics

from .models import Kanji
from .serializers import KanjiSerializer

class KanjiOverviewView(views.APIView):
    def get(self, request, format=None):
        return response.Response({
            'total_kanji': Kanji.objects.count()
        }, status=200)


class KanjiDetailView(generics.RetrieveAPIView):
    queryset = Kanji.objects.all()
    serializer_class = KanjiSerializer
    lookup_field = 'writing'
