# Generated by Django 5.1.1 on 2024-10-06 20:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_job'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicant_name', models.CharField(max_length=150)),
                ('applicant_email', models.EmailField(max_length=254)),
                ('cover_letter', models.FileField(blank=True, null=True, upload_to='cover_letters/')),
                ('proposal', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='myapp.job')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='myapp.user')),
            ],
        ),
    ]
