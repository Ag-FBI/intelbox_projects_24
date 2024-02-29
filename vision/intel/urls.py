from django.urls import path, include
from .import views

app_name = 'intel'
urlpatterns = [
    path("", views.UserView.as_view(), name="list_view"),
    path("<int:pk>/", views.UserView.as_view(), name="detail_list"),
    path("image/", views.ImageView.as_view(), name="image"),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name="logout")
]