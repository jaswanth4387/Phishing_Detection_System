from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('redirect/', views.post_login_redirect, name='post_login_redirect'),
    path('predict/', views.predict_view, name='predict'),
    path('profile/', views.profile_view, name='profile'),

    path('forgot/', views.forgot_password, name='forgot_password'),
    path('verify-otp/', views.verify_otp, name='verify_otp'),
    path('reset/', views.reset_password, name='reset_password'),
    path('adminlogin/', views.admin_login_view, name='admin_login'),
]