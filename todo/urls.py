from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('created', views.CreatedView.as_view()),
]
