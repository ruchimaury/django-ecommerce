from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('buy/', views.buy),
    path('success/<int:order_id>/', views.success),
]