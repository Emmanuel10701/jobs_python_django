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
    ApplicationDetailView,
    ForgotPasswordView,
    ResetPasswordConfirmView,
    FreelancerProfileView,
    ClientProfileCreateView,
    ClientProfileRetrieveUpdateView,
)
from rest_framework_simplejwt.views import TokenRefreshView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Authentication URLs
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Password Reset
    path('auth/forgot-password/', ForgotPasswordView.as_view(), name='forgot-password'),
    path('auth/reset-password/<str:uidb64>/<str:token>/', ResetPasswordConfirmView.as_view(), name='password_reset_confirm'),

    # Freelancer Profile
    path('freelancer/profile/', FreelancerProfileView.as_view(), name='freelancer-profile'),

    # Client Profile
    path('api/client/profile/', ClientProfileCreateView.as_view(), name='client-profile-create'),
    path('api/client/profile/<int:pk>/', ClientProfileRetrieveUpdateView.as_view(), name='client-profile-detail'),

    # Users
    path('users/', UserListView.as_view(), name='user-list'),
    path('auth/users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),

    # Applications
    path('applications/', ApplicationListCreateView.as_view(), name='application-list-create'),
    path('applications/<int:pk>/', ApplicationDetailView.as_view(), name='application-detail'),

    # Contact and Subscriptions
    path('api/contact/', ContactView.as_view(), name='contact'),
    path('subscribe/', SubscriptionView.as_view(), name='subscribe'),

    # Job Listings
    path('api/jobs/', JobListCreateAPIView.as_view(), name='job-list-create'),
    path('api/jobs/<int:pk>/', JobDetailAPIView.as_view(), name='job-detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
