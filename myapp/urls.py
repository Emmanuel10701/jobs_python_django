from django.urls import path
from .views import RegisterView, CustomTokenObtainPairView, UserListView, UserDetailView
from .views import ContactView
from .views import SubscriptionView
from .views import JobListCreateAPIView, JobDetailAPIView,   ApplicationListCreateView,ApplicationDetailView
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', CustomTokenObtainPairView.as_view(), name='login'),

    path('applications/', ApplicationListCreateView.as_view(), name='application-list-create'),
    path('applications/<int:pk>/', ApplicationDetailView.as_view(), name='application-detail'),


     path('api/contact/', ContactView.as_view(), name='contact'),
    path('subscribe/', SubscriptionView.as_view(), name='subscribe'),
     path('api/jobs/', JobListCreateAPIView.as_view(), name='job-list-create'),  # List and create
    path('api/jobs/<int:pk>/', JobDetailAPIView.as_view(), name='job-detail'),  # Retrieve, update, delete
    path('users/', UserListView.as_view(), name='user-list'),
    path('auth/users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
