from django.urls import path
from .views import *


app_name = 'blog'

urlpatterns = [
    path('',index,name="index"),
    path('detail/<int:pk>',ProductDetailView.as_view(),name='detail'),
    path('signup/', signupPage, name='signup'),
    path('login/', loginPage, name='login')
]