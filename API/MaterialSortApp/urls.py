from django.urls import path
from .views import RecognitionResultListCreate

urlpatterns = [
    path('results/', RecognitionResultListCreate.as_view(), name='recognition-result-list'),
]