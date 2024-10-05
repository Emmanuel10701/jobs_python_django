from rest_framework import serializers
from .models import User
from .models import Subscription

from .models import Job

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['email']


class ContactSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    message = serializers.CharField()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'role']

    def create(self, validated_data):
        # No hashing, just save the password as is
        user = User(**validated_data)
        user.save()
        return user
