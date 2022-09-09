from django.urls import path
from . import views

urlpatterns = [
    path('minis/', views.mini_list),
    path('minis/<int:pk>/', views.mini_detail),
    path('packs', views.pack_list),
    path('packs/<int:pk>/', views.pack_detail)
]
