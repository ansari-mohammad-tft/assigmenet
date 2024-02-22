from backend.router import router
from django.urls import path

from .views import TopWordsView, SearchHistoryView

app_name = 'wiki'
router.register(r'top-words', TopWordsView, basename="create-top-words")
router.register(r'search-history', SearchHistoryView, basename="search_history")
