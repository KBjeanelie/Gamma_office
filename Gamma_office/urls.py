"""
URL configuration for Gamma_office project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from API.views.auth import LoginView, LogoutView, PasswordChangeView, PasswordResetView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('Gamma/Office/Admin/', admin.site.urls),
    path('Gamma/Office/Compte/', include('Compte.urls')),
    
    re_path('api/', include('API.urls')),
    #path('api-auth/', include('rest_framework.urls')),
    #path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/login/', LoginView.as_view(), name='api-login'),
    path('api/logout/', LogoutView.as_view(), name='api-logout'),
    path('api/reset-password/', PasswordResetView.as_view(), name='api-reset-password'),
    path('api/change-password/', PasswordChangeView.as_view(), name='api-change-password'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
