# Generated by Django 4.1.7 on 2023-03-14 06:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_user_profile_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='employer',
        ),
        migrations.AddField(
            model_name='application',
            name='jobs',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.listjobs'),
        ),
        migrations.AlterField(
            model_name='application',
            name='employee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.employee'),
        ),
    ]