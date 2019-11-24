from django.urls import path
from .views import KanjiOverviewView
from .views import KanjiDetailView

urlpatterns = [
    path('', KanjiOverviewView.as_view(), name='kanji-overview'),
    path('<str:writing>', KanjiDetailView.as_view(), name='kanji-detail')
]
