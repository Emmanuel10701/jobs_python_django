# Generated by Django 5.0.1 on 2024-10-19 06:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_application_company_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='company_name',
        ),
    ]