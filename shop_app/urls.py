from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('info/<int:pk>/', info, name="info"),
    path('addcomment/<int:pk>/', addcomment, name="addcomment"),

    path('login/', loginPage, name="login"),

    path('register/', registerPage, name="register"),
    
    path('logout/', logoutUser, name="logout"),

    path('mycart/', mycart, name='mycart'),

    path('addtocart/<int:pk>/', addtocart, name='addtocart'),
    path('update/<int:pk>/', update, name='update'),

    path('order/', order, name='order'),
    path('addorder/', addOrder, name='addorder'),









]

