from django.urls import path
from . import views  # Make sure there is a space after the dot

urlpatterns = [
    path('', views.index, name='index'),  # Temporary placeholder
]
