from django.shortcuts import render

from rest_framework import generics
from .models import Query, Result
from .serializers import QuerySerializer, ResultSerializer

class QueryListCreateView(generics.ListCreateAPIView):
    queryset = Query.objects.all()
    serializer_class = QuerySerializer

class ResultCreateView(generics.CreateAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer

class QueryHistoryView(generics.ListAPIView):
    serializer_class = QuerySerializer

    def get_queryset(self):
        cadaster_number = self.request.query_params.get('cadaster_number', None)
        if cadaster_number:
            return Query.objects.filter(cadaster_number=cadaster_number)
        return Query.objects.all()