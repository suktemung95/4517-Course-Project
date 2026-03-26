from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_card, name='upload'),
    path('', views.home, name='home'),
    path('image-search/', views.image_search, name='image_search'),
    path('db/', views.show_db),
    path("delete/<int:card_id>/", views.delete_card, name="delete_card"),
]