import os

from datetime import datetime
from django.shortcuts import render
from rest_framework import views
from rest_framework import response
from rest_framework import generics

from .models import Kanji
from .models import Vocabulary
from .serializers import KanjiSerializer
from .serializers import VocabularySerializer
from .image_file_utils import save_base64_to_file
from clients.s3.s3_manager import S3ImageManager

IMAGE_DIR = 'images-data'

class KanjiOverviewView(generics.ListAPIView):
    queryset = Kanji.objects.all()
    serializer_class = KanjiSerializer
    lookup_field = 'writing'


class KanjiDetailView(generics.RetrieveAPIView):
    queryset = Kanji.objects.all()
    serializer_class = KanjiSerializer
    lookup_field = 'writing'


class VocabularyOverviewView(views.APIView):
    def get(self, request, format=None):
        return response.Response({
            'total_vocabulary': Vocabulary.objects.count()
        }, status=200)


class VocabularyDetailView(generics.RetrieveAPIView):
    queryset = Vocabulary.objects.all()
    serializer_class = VocabularySerializer
    lookup_field = 'writing'


class RecognizeImageView(views.APIView):
    def post(self, request, format=None):
        base64_data = request.data.get('imageData')
        # Not yet recognize the image
        result = '一'
        folder = '{}/{}'.format(IMAGE_DIR, result)
        os.system('mkdir -p {}'.format(folder))
        filename = '{}-{}'.format('user', datetime.now().strftime("%Y%m%d-%H%M%S"))
        full_name = save_base64_to_file(base64_data, folder, filename)
        s3_manager = S3ImageManager()
        url = s3_manager.upload_image(folder, full_name)
        print ('URL: ', url)
        return response.Response(result, status=200)


class SaveTrainingImageView(views.APIView):
    def post(self, request, format=None):
        base64_data = request.data.get('imageData')
        kanji = request.data.get('kanji')
        print (kanji)
        folder = '{}/{}'.format(IMAGE_DIR, kanji)
        os.system('mkdir -p {}'.format(folder))
        filename = '{}-{}'.format('user', datetime.now().strftime("%Y%m%d-%H%M%S"))
        full_name = save_base64_to_file(base64_data, folder, filename)
        s3_manager = S3ImageManager()
        url = s3_manager.upload_image(folder, full_name)
        return response.Response(url, status=200)