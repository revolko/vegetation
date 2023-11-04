from rest_framework.authtoken import views as rest_views

from django.urls import path

from . import views

urlpatterns = [
    path('register', views.RegisterUserView.as_view()),
    path('login', rest_views.obtain_auth_token),
]
