from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .models import User, Subscription, Job, Application
from .serializers import UserSerializer, SubscriptionSerializer, JobSerializer, ApplicationSerializer,ContactSerializer
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.views import APIView

from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from django.http import JsonResponse
from django.contrib.auth.tokens import default_token_generator
from rest_framework.views import APIView
from .models import User




from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.encoding import force_str


class ResetPasswordConfirmView(APIView):
    permission_classes = [AllowAny]  # Allow anyone to access this view

    def post(self, request, uidb64, token):
        try:
            # Decode the uid and find the corresponding user
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)

            # Check if the token is valid
            if not default_token_generator.check_token(user, token):
                return Response({'error': 'Invalid token or token has expired.'}, status=status.HTTP_400_BAD_REQUEST)

            # Get new password from request
            new_password = request.data.get('new_password')
            confirm_password = request.data.get('confirm_password')

            if new_password != confirm_password:
                return Response({'error': 'Passwords do not match.'}, status=status.HTTP_400_BAD_REQUEST)

            # Set new password
            user.set_password(new_password)
            user.save()

            return Response({'message': 'Password has been reset successfully.'}, status=status.HTTP_200_OK)

        except (User.DoesNotExist, ValueError):
            return Response({'error': 'Invalid request or user does not exist.'}, status=status.HTTP_400_BAD_REQUEST)


class ForgotPasswordView(APIView):
    permission_classes = [AllowAny]  # Ensure anyone can access this

    def post(self, request):
        email = request.data.get('email')
        if not email:
            return JsonResponse({'error': 'Email is required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return JsonResponse({'error': 'User with this email does not exist.'}, status=status.HTTP_400_BAD_REQUEST)

        # Generate token and UID
        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))

        # Generate reset password URL
        reset_url = f"http://localhost:5173/reset-password/{uid}/{token}/"

        try:
            # Send password reset email
            send_mail(
                'Password Reset',
                f'Click the following link to reset your password: {reset_url}',
                settings.EMAIL_HOST_USER,  # Use the configured email host user
                [email],
                fail_silently=False,
            )
            return JsonResponse({'message': 'Password reset email has been sent.'}, status=status.HTTP_200_OK)

        except Exception as e:
            return JsonResponse({'error': f'Failed to send email: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def post(self, request):
        email = request.data.get('email')
        try:
            user = User.objects.get(email=email)
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            reset_url = f"http://localhost:5173/reset-password/{uid}/{token}/"
            send_mail(
                'Password Reset',
                f'Click the following link to reset your password: {reset_url}',
                'noreply@example.com',
                [email],
            )
            return JsonResponse({'message': 'Password reset email has been sent.'}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return JsonResponse({'error': 'User with this email does not exist.'}, status=status.HTTP_400_BAD_REQUEST)



class CustomTokenObtainPairView(TokenObtainPairView):
    permission_classes = [AllowAny]  # Allow anyone to access this view

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)


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
    permission_classes = [AllowAny]  # Changed to AllowAny


class ApplicationListCreateView(generics.ListCreateAPIView):
    permission_classes = [AllowAny]  # Allow anyone to access this view
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer


class ApplicationDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]  # Allow anyone to access this view
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer


# List and Create jobs
class JobListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [AllowAny]  # Allow anyone to access this view
    queryset = Job.objects.all()
    serializer_class = JobSerializer


# Retrieve, Update, and Delete a specific job
class JobDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]  # Allow anyone to access this view
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class SubscriptionView(APIView):
    permission_classes = [AllowAny]  # Allow anyone to access this view

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


class ContactView(APIView):
    permission_classes = [AllowAny]  # Allow anyone to access this view

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
