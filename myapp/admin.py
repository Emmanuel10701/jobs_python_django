from django.contrib import admin
from .models import User, Subscription, Job, Application

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role')
    search_fields = ('username', 'email')
    list_filter = ('role',)
    
@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('email',)
    search_fields = ('email',)

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'company_name', 'user', 'created_at')
    search_fields = ('job_title', 'company_name', 'location')
    list_filter = ('work_type', 'created_at')

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('applicant_name', 'job', 'created_at')
    search_fields = ('applicant_name', 'applicant_email', 'proposal')
    list_filter = ('created_at',)
