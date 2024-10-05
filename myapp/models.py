from django.db import models

class User(models.Model):
    USER_ROLES = (
        ('client', 'Client'),
        ('freelancer', 'Freelancer'),
    )

    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Store passwords in plaintext (not recommended)
    role = models.CharField(max_length=10, choices=USER_ROLES)

    def __str__(self):
        return self.username
    
class Subscription(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email