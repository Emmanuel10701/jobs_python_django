from rest_framework import serializers
from .models import User, Subscription, Job, Application,Contact

# Serializer for the User model with only required fields
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'role']
        extra_kwargs = {
            'password': {'write_only': True}  # To ensure password is write-only and not included in responses
        }

    # Hash the password when creating a new user
    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            role=validated_data['role']
        )
        user.set_password(validated_data['password'])  # Hash the password
        user.save()
        return user

    # Hash the password when updating a user
    def update(self, instance, validated_data):
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])  # Hash the password if it is being updated
        return super().update(instance, validated_data)

# Serializer for the Subscription model
class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['id', 'email']

# Serializer for the Job model
class JobSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Job
        fields = [
            'id', 'user', 'job_title', 'company_name', 'email', 'mobile', 
            'description', 'requirements', 'salary', 'logo', 
            'location', 'work_type', 'created_at'
        ]

# Serializer for the Application model
class ApplicationSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    job = JobSerializer(read_only=True)

    class Meta:
        model = Application
        fields = [
            'id', 'user', 'job', 'applicant_name', 'applicant_email', 
            'cover_letter', 'proposal', 'created_at'
        ]
# Contact Serializer
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']

    def create(self, validated_data):
        return Contact.objects.create(**validated_data)
