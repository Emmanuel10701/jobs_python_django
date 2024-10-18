from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from rest_framework.views import APIView
from .models import User, Subscription, Job, Application, FreelancerProfile, ClientProfile
from .serializers import UserSerializer, SubscriptionSerializer, JobSerializer,ContactSerializer, ApplicationSerializer, FreelancerProfileSerializer, ClientProfileSerializer
from django.http import JsonResponse
from django.utils.http import urlsafe_base64_decode


# Password Reset Views
class ForgotPasswordView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        email = request.data.get('email')
        if not email:
            return JsonResponse({'error': 'Email is required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(email=email)
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            reset_url = f"http://localhost:5173/reset-password/{uid}/{token}/"
            send_mail(
                'Password Reset',
                f'Click the following link to reset your password: {reset_url}',
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
            return JsonResponse({'message': 'Password reset email has been sent.'}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return JsonResponse({'error': 'User with this email does not exist.'}, status=status.HTTP_400_BAD_REQUEST)


class ResetPasswordConfirmView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)

            if not default_token_generator.check_token(user, token):
                return Response({'error': 'Invalid token or token has expired.'}, status=status.HTTP_400_BAD_REQUEST)

            new_password = request.data.get('new_password')
            confirm_password = request.data.get('confirm_password')

            if not new_password or not confirm_password:
                return Response({'error': 'Both new password and confirm password are required.'}, status=status.HTTP_400_BAD_REQUEST)

            if new_password != confirm_password:
                return Response({'error': 'Passwords do not match.'}, status=status.HTTP_400_BAD_REQUEST)

            user.set_password(new_password)
            user.save()

            return Response({'message': 'Password has been reset successfully.'}, status=status.HTTP_200_OK)

        except (ValueError, TypeError):
            return Response({'error': 'Invalid UID.'}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({'error': 'User does not exist.'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

# Token Authentication View
class CustomTokenObtainPairView(TokenObtainPairView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)

# User Registration View
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

# User List and Detail Views
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

# Job Views
class JobListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class JobDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Job.objects.all()
    serializer_class = JobSerializer

# Application Views
class ApplicationListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

class ApplicationDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

# Subscription Views
class SubscriptionView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = SubscriptionSerializer(data=request.data)
        if serializer.is_valid():
            subscription = serializer.save()

            subject = 'Subscription Confirmation'
            message = f'Thank you for subscribing! We have received your email: {subscription.email}'
            recipient_list = [subscription.email]

            try:
                send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list)
                return Response({'message': 'Subscribed successfully! 🎉'}, status=status.HTTP_201_CREATED)
            except Exception:
                return Response({'message': 'Subscribed successfully, but failed to send email notification.'}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        subscriptions = Subscription.objects.all()
        subscription_list = [{'id': sub.id, 'email': sub.email} for sub in subscriptions]
        return Response({'subscriptions': subscription_list, 'message': 'Thank you for your subscription!'}, status=status.HTTP_200_OK)

# Profile Views
class ClientProfileCreateView(generics.CreateAPIView):
    queryset = ClientProfile.objects.all()
    serializer_class = ClientProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

class ClientProfileRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = ClientProfile.objects.all()
    serializer_class = ClientProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

class FreelancerProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        profile = FreelancerProfile.objects.get(user=request.user)
        serializer = FreelancerProfileSerializer(profile)
        return Response(serializer.data)

    def put(self, request):
        profile = FreelancerProfile.objects.get(user=request.user)
        serializer = FreelancerProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def post(self, request):
        serializer = FreelancerProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

# Contact View
class ContactView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data['name']
            email = serializer.validated_data['email']
            message = serializer.validated_data['message']

            try:
                send_mail(
                    f"Contact Form Submission from {name}",
                    message,
                    email,
                    ['recipient@example.com'],  # Change to your recipient email
                    fail_silently=False,
                )
                confirmation_subject = "We Have Received Your Message!"
                confirmation_message = f"Thank you, {name}! We have received your message and will get back to you shortly."
                send_mail(
                    confirmation_subject,
                    confirmation_message,
                    'no-reply@example.com',
                    [email],
                    fail_silently=False,
                )
                return Response({"message": f"Thank you, {name}! Your message has been sent successfully. 😊"}, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({"error": f"An error occurred while sending your message: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
