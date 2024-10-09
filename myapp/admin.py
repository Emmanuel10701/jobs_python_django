from django.contrib import admin
from .models import User, Job, ClientProfile, FreelancerProfile, Application

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'is_active', 'date_joined')
    search_fields = ('username', 'email')
    list_filter = ('role', 'is_active')

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'company_name', 'user', 'created_at', 'work_type')
    search_fields = ('job_title', 'company_name', 'location')
    list_filter = ('work_type', 'created_at')
    
    def created_at(self, obj):
        return obj.created_at  # Add this method if 'created_at' is a field in your Job model.

@admin.register(ClientProfile)
class ClientProfileAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'contact_name', 'email', 'phone_number')
    search_fields = ('company_name', 'contact_name', 'email')

@admin.register(FreelancerProfile)
class FreelancerProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone_number', 'nationality')
    search_fields = ('full_name', 'email')

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('applicant_name', 'job', 'created_at')
    search_fields = ('applicant_name', 'job__job_title')
    list_filter = ('created_at',)

