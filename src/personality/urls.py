from django.urls import path
from .views import *

urlpatterns = [
    path('persona', PersonalityPrediction.as_view(), name='personality'),
]