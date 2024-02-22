from django.shortcuts import render
from rest_framework import viewsets, mixins

from .models import TopWordsModel
from .serializer import TopWordsModelSerializer


# Create your views here.

class TopWordsView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = TopWordsModelSerializer
    queryset = TopWordsModel.objects.all()
    permission_classes = []
    authentication_classes = []


class SearchHistoryView(viewsets.ReadOnlyModelViewSet):
    serializer_class = TopWordsModelSerializer
    queryset = TopWordsModel.objects.all()
