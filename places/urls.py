from django.urls import path
from . import views

urlpatterns = [
    path('places/', views.get_places),
    path('places/add/', views.add_place),
    path('places/<int:place_id>/rate/', views.add_rating),
]