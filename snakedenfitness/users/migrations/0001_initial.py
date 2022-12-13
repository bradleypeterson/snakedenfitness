# Generated by Django 4.1.2 on 2022-12-13 01:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('birth_date', models.DateField(blank=True, default='1960-01-01')),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('avatar', models.ImageField(blank=True, default='avatars/generic-avatar.png', null=True, upload_to='avatars/')),
                ('role', models.SmallIntegerField(blank=True, choices=[(0, 'Client'), (1, 'Dietician'), (2, 'Trainer')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='clientTrainer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='T_assigned_client', to=settings.AUTH_USER_MODEL, unique=True)),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='T_assigned_trainer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='clientDieter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='D_assigned_client', to=settings.AUTH_USER_MODEL, unique=True)),
                ('dieter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='D_assigned_dietician', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
