from . import views
from django.urls import path



#path goes here
urlpatterns = [
    path('', views.cart, name='cart' ),
]
