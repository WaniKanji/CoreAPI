from django.urls import path
from .views import KanjiOverviewView
from .views import KanjiDetailView
from .views import VocabularyOverviewView
from .views import VocabularyDetailView
from .views import RecognizeImageView
from .views import SaveTrainingImageView

urlpatterns = [
    # Kanji
    path('kanji/', KanjiOverviewView.as_view(), name='kanji-overview'),
    path('kanji/<str:writing>', KanjiDetailView.as_view(), name='kanji-detail'),
    path('vocabulary/', VocabularyOverviewView.as_view(), name='vocabulary-overview'),
    path('vocabulary/<str:writing>', VocabularyDetailView.as_view(), name='vocabulary-detail'),
    path('recognize/', RecognizeImageView.as_view(), name='recognize'),
    path('save-training-image/', SaveTrainingImageView.as_view(), name='save-training-image'),
]
