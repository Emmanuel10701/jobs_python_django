from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import User
from rest_framework import status
from .serializers import ContactSerializer
from django.core.mail import send_mail
from rest_framework.views import APIView

from .serializers import UserSerializer
from .models import Subscription
from .serializers import SubscriptionSerializer

class SubscriptionView(APIView):
    def post(self, request):
        serializer = SubscriptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Subscribed successfully!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# User registration
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

# List all users
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

# Get, Update, and Delete a single user
class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

# Custom Token Obtain Pair View for Login
class CustomTokenObtainPairView(TokenObtainPairView):
        permission_classes = [AllowAny]




class ContactView(APIView):
    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data['name']
            email = serializer.validated_data['email']
            message = serializer.validated_data['message']

            # Send email
            try:
                send_mail(
                    f"Contact Form Submission from {name}",
                    message,
                    email,  # From email
                    ['recipient@example.com'],  # To email (change to your recipient)
                    fail_silently=False,
                )
                # Send a confirmation message back to the user
                return Response({
                    "message": f"Thank you, {name}! Your message has been sent successfully."
                }, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({
                    "error": f"An error occurred while sending your message: {str(e)}"
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

