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
from django.core.mail import send_mail
from django.conf import settings



from .models import Job
from .serializers import JobSerializer

# List and Create jobs
class JobListCreateAPIView(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

# Retrieve, Update, and Delete a specific job
class JobDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer




    
class SubscriptionView(APIView):
    def post(self, request):
        serializer = SubscriptionSerializer(data=request.data)
        if serializer.is_valid():
            subscription = serializer.save()

            # Send notification email
            subject = 'Subscription Confirmation'
            message = f'Thank you for subscribing! We have received your email: {subscription.email}'
            recipient_list = [subscription.email]  # Send to the subscriber
            try:
                send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list)
            except Exception as e:
                return Response({'message': 'Subscribed successfully, but failed to send email notification.'}, status=status.HTTP_201_CREATED)

            return Response({'message': 'Subscribed successfully! 🎉'}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        subscriptions = Subscription.objects.all()
        subscription_list = [{'id': sub.id, 'email': sub.email} for sub in subscriptions]
        return Response({'subscriptions': subscription_list, 'message': 'We have received your email subscription! Thank you! 😊'}, status=status.HTTP_200_OK)


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

            # Prepare the email to the recipient
            try:
                send_mail(
                    f"Contact Form Submission from {name}",
                    message,
                    email,  # From email
                    ['recipient@example.com'],  # Change this to your actual recipient email
                    fail_silently=False,
                )

                # Prepare the confirmation email back to the sender
                confirmation_subject = "We Have Received Your Message!"
                confirmation_message = f"Thank you, {name}! We have received your message and will get back to you shortly."
                send_mail(
                    confirmation_subject,
                    confirmation_message,
                    'no-reply@example.com',  # Use a no-reply or your actual sender email
                    [email],  # Send to the user's email
                    fail_silently=False,
                )

                return Response({
                    "message": f"Thank you, {name}! Your message has been sent successfully. 😊"
                }, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({
                    "error": f"An error occurred while sending your message: {str(e)}"
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
