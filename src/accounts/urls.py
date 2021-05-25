from django.urls import path, include

from .views import CustomPasswordResetView, CustomPasswordResetConfirmView


urlpatterns = [
    path('', include('dj_rest_auth.urls')),
]