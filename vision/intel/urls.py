from django.urls import path, include
from .import views

app_name = 'intel'
urlpatterns = [
    path("", views.test_response),
    path("<int:pk>/", views.test_response)
]