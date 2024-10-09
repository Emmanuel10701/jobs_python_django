from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have a username")
        
        user = self.model(
            username=username,
            email=self.normalize_email(email),
        )
        user.set_password(password)  # Use set_password to hash the password
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        user = self.create_user(
            username,
            email,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    USER_ROLES = (
        ('client', 'Client'),
        ('freelancer', 'Freelancer'),
    )
    
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=USER_ROLES)
    is_active = models.BooleanField(default=True)  # User account status
    is_staff = models.BooleanField(default=False)  # User staff status
    date_joined = models.DateTimeField(auto_now_add=True, null=True)



    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email'] 

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

    class Meta:
        verbose_name = "Job"
        verbose_name_plural = "Jobs"
        ordering = ['created_at']

    def __str__(self):
        return self.job_title

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.email}"

class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications')
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    applicant_name = models.CharField(max_length=150)
    applicant_email = models.EmailField()
    cover_letter = models.FileField(upload_to='cover_letters/', blank=True, null=True)
    proposal = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Application"
        verbose_name_plural = "Applications"
        ordering = ['created_at']

    def __str__(self):
        return f"{self.applicant_name} applied for {self.job.job_title}"
