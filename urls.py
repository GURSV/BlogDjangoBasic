from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from .views import profile_view

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('accounts/profile/', profile_view, name='profile'),
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('search/', views.search_view, name='search'),
]
