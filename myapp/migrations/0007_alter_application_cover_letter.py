# Generated by Django 5.1.2 on 2024-10-13 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_job_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='cover_letter',
            field=models.FileField(null=True, upload_to='cover_letters/'),
        ),
    ]