from django.urls import path
from . import views

urlpatterns = [
    path('minis/', views.MiniListAPIView.as_view(), name='mini-list'),
    path('minis/<int:pk>/', views.MiniDetailAPIView.as_view(), name='mini-detail'),
    path('packs/', views.PackListAPIView.as_view(), name='pack-list'),
    path('packs/<int:pk>/', views.PackDetailAPIView.as_view(), name='pack-detail')
]
