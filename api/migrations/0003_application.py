# Generated by Django 4.1.7 on 2023-03-08 09:02

import api.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=50)),
                ('role', models.CharField(max_length=100)),
                ('date_applied', models.DateTimeField(auto_now_add=True)),
                ('cv', models.FileField(default='cv.pdf', upload_to='api/application', validators=[api.validators.validate_file_size, django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'png', 'jpg'])])),
                ('socials', models.URLField()),
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.employee')),
                ('employer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.employer')),
            ],
        ),
    ]
