# Generated by Django 5.1.4 on 2024-12-10 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locationtrack', '0004_alter_attendance_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='country',
        ),
    ]
