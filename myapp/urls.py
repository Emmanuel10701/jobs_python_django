from django.urls import path
from .views import RegisterView, CustomTokenObtainPairView, UserListView
from .views import  UserListView, UserDetailView


urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/', UserListView.as_view(), name='user-list'),  # New endpoint for getting all users
    path('auth/users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),  # Single user operation
]
