# Generated by Django 4.1.2 on 2022-12-05 23:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0003_pic'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Document',
        ),
        migrations.RenameField(
            model_name='pic',
            old_name='display_picture',
            new_name='Upload',
        ),
    ]
