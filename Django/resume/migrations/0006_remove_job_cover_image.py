# Generated by Django 2.2 on 2019-04-16 01:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0005_school'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='cover_image',
        ),
    ]
