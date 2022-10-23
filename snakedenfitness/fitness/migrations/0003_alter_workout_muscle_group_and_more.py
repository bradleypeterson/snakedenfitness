# Generated by Django 4.1.1 on 2022-10-23 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitness', '0002_workout'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='muscle_group',
            field=models.CharField(choices=[('arms', 'Arms'), ('shoulders', 'Shoulders'), ('back', 'Back'), ('core', 'Core'), ('legs', 'Legs')], max_length=50),
        ),
        migrations.AlterField(
            model_name='workout',
            name='workout_type',
            field=models.CharField(choices=[('cardio', 'Cardio'), ('strength', 'Strength'), ('endurance', 'Endurance')], max_length=50),
        ),
    ]
