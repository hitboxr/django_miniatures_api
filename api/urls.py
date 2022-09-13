from django.urls import path
from . import views

urlpatterns = [
    path('minis/', views.MiniListAPIView.as_view()),
    path('minis/<int:pk>/', views.MiniDetailAPIView.as_view()),
    path('packs/', views.PackListAPIView.as_view()),
    path('packs/<int:pk>/', views.PackDetailAPIView.as_view())
]
