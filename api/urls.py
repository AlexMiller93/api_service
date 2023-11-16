from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('query/', views.QueryListCreateView.as_view(), name='query-list-create'),
    path('result/', views.ResultCreateView.as_view(), name='result-create'),
    path('history/', views.QueryHistoryView.as_view(), name='query-history'),
]