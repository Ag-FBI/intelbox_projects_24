from django.urls import path
from .views import *

urlpatterns = [
    path('process_frame/', info),
]