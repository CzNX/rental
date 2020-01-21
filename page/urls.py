from django.urls import path
from .import views
from django.contrib.auth import views as auth_views


urlpatterns = [
  path('', views.home, name='home'),
  path('login', views.login, name='login'),
  # path('login', auth_views.LoginView.as_view(),name='login'),
  # path('logout', auth_views.LogoutView.as_view(),name='logout'),
  path('logout', views.logout, name='logout'),
  path('register', views.register, name='register'),
  path('profile', views.profile, name='profile'),

]