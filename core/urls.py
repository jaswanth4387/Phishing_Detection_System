from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Include app URLs ONLY (clean architecture)
    path('', include('client_portal.urls')),
    path('', include('admin_dashboard.urls')),

    # Auth (only once)
    path('logout/', LogoutView.as_view(), name='logout'),
]