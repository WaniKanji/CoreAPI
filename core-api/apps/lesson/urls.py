from django.urls import path
from .views import KanjiOverviewView
from .views import KanjiDetailView

urlpatterns = [
    # Kanji
    path('kanji/', KanjiOverviewView.as_view(), name='kanji-overview'),
    path('kanji/<str:writing>', KanjiDetailView.as_view(), name='kanji-detail')
]
