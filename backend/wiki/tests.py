import json
import time

from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from datetime import datetime
from .models import TopWordsModel
from django.test import TestCase, Client

client = Client()


class TopWordsViewTest(APITestCase):
    def test_create_top_words(self):
        data = {'topic': 'django', 'n': 2}
        url = reverse('create-top-words-list')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(TopWordsModel.objects.count(), 1)
        top_words_instance = TopWordsModel.objects.get()
        self.assertEqual(top_words_instance.topic, 'django')
        self.assertEqual(top_words_instance.n, 2)
        self.assertIsNotNone(top_words_instance.top_words)
        self.assertEqual(len(top_words_instance.top_words), 2)
        self.assertIsInstance(top_words_instance.created_at, datetime)


class SearchHistoryViewTest(APITestCase):
    def test_list_search_history(self):
        top_words1 = [
            {'word': 'the', 'count': 16},
            {'word': 'of', 'count': 9}]
        top_words2 = [
            {'word': 'the', 'count': 16},
            {'word': 'of', 'count': 9},
            {'word': 'ok', 'count': 9}
        ]
        TopWordsModel.objects.create(topic='topic1', n=2, top_words=top_words1)
        TopWordsModel.objects.create(topic='topic2', n=3, top_words=top_words2)

        url = reverse('search_history-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['topic'], 'topic1')
        self.assertEqual(response.data[0]['top_words'], top_words1)
        self.assertEqual(response.data[1]['topic'], 'topic2')
        self.assertEqual(response.data[1]['top_words'], top_words2)
