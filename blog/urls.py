from django.urls import path
from .views import *


app_name = 'blog'

urlpatterns = [
    path('',index,name="index"),
    path('signup/', signupPage, name='signup'),
    path('login/', loginPage, name='login'),
    path('eltuvchi/', eltuvchiPage, name='postman'),
    path('offer/<int:pk>/', offerDetailPage, name='offer'),
    path('p/<str:slug>/',productDetail, name='product'),
    path('logout/', logoutPage),
    path('offers',offers, name="offers"),
    path('main',main,name='main'),
    path('search_product',search_product,name="search_product")

]