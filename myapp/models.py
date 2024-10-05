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

class Job(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='jobs')
    job_title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    email = models.EmailField()
    mobile = models.CharField(max_length=20)
    description = models.TextField()
    requirements = models.TextField()
    salary = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    location = models.CharField(max_length=100)
    work_type = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.job_title