from . import views
from django.urls import path


# path goes here
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.dashboard, name='dashboard'),
    
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    
]
