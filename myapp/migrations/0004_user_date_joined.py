# Generated by Django 5.1.1 on 2024-10-09 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_application_options_alter_job_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
