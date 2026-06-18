from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('login/', views.login_view),
    path('register/', views.register_view),
    path('logout/', views.logout_view),
    path('suggestions/', views.suggestions),
    path('about/', views.about),
    path('api/gifts/search/', views.gift_search_api),
]