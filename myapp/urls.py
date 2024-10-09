from django.urls import path
from .views import (
    RegisterView,
    UserListView,
    UserDetailView,
    ContactView,
    SubscriptionView,     
    CustomTokenObtainPairView,
    JobListCreateAPIView,
    JobDetailAPIView,
    ApplicationListCreateView,
    ApplicationDetailView
)
from rest_framework_simplejwt.views import TokenRefreshView  # JWT views for login and token refresh

from django.conf import settings
from django.conf.urls.static import static

from .views import ForgotPasswordView



urlpatterns = [
    # Authentication
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
#forgot pasword 
    path('auth/forgot-password/', ForgotPasswordView.as_view(), name='forgot-password'),

    # Users
    path('users/', UserListView.as_view(), name='user-list'),
    path('auth/users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),

    # Applications
    path('applications/', ApplicationListCreateView.as_view(), name='application-list-create'),
    path('applications/<int:pk>/', ApplicationDetailView.as_view(), name='application-detail'),

    # Contact and Subscriptions
    path('api/contact/', ContactView.as_view(), name='contact'),
    path('subscribe/', SubscriptionView.as_view(), name='subscribe'),

    # Jobs
    path('api/jobs/', JobListCreateAPIView.as_view(), name='job-list-create'),  # List and create jobs
    path('api/jobs/<int:pk>/', JobDetailAPIView.as_view(), name='job-detail'),  # Retrieve, update, delete specific job
]

# Static and media files handling in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
