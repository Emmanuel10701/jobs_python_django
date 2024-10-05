from django.urls import path
from .views import RegisterView, CustomTokenObtainPairView, UserListView, UserDetailView
from .views import ContactView
from .views import SubscriptionView



urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', CustomTokenObtainPairView.as_view(), name='login'),
     path('api/contact/', ContactView.as_view(), name='contact'),
    path('subscribe/', SubscriptionView.as_view(), name='subscribe'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('auth/users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
]
