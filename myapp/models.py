from django.db import models

class User(models.Model):
    USER_ROLES = (
        ('client', 'Client'),
        ('freelancer', 'Freelancer'),
    )

    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Store hashed passwords in production
    role = models.CharField(max_length=10, choices=USER_ROLES)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'role'] 
    
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


class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications')
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    applicant_name = models.CharField(max_length=150)
    applicant_email = models.EmailField()
    cover_letter = models.FileField(upload_to='cover_letters/', blank=True, null=True)
    proposal = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.applicant_name} applied for {self.job.job_title}"
