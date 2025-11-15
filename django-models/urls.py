from django.urls import path
from .import views

urlpatterns = [
    # Temporary placeholder view
    path('', views.index, name='index'),
]

