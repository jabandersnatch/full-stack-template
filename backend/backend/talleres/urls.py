from django.urls import path, include
from .views import *

urlpatterns = [
    path('get_files/', get_files),
    path('reto_1/<str:filename>', reto_1)
]

