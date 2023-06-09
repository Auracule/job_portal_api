# Generated by Django 4.1.7 on 2023-03-17 12:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_remove_application_employer_application_jobs_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogCat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
                ('body', models.TextField()),
                ('published', models.DateTimeField(default=django.utils.timezone.now)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('blogcat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.blogcat')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('comment', models.TextField()),
                ('post_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('blogpost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.blogpost')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
