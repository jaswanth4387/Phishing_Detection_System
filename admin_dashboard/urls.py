from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('users/', views.view_users, name='view_users'),
    path('predictions/', views.view_predictions, name='view_predictions'),
    path('ratio/', views.ratio_view, name='ratio'),
    path('charts/', views.charts_view, name='charts'),
    path('accuracy/', views.accuracy_view, name='accuracy'),
    path('train/', views.train_model, name='train_model'),
]