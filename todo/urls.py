from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('created', views.CreatedView.as_view(), name='created'),
]
