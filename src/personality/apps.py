import os
import joblib
from django.apps import AppConfig
from django.conf import settings

class PersonalityConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'personality'
    MODEL_FILE = os.path.join(settings.MODELS, "BigFivePersonalityModel.joblib")
    model = joblib.load(MODEL_FILE)