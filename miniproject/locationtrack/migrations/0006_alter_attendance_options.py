# Generated by Django 5.1.4 on 2024-12-17 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locationtrack', '0005_remove_attendance_country'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attendance',
            options={'ordering': ['-timestamp'], 'verbose_name_plural': 'Attendances'},
        ),
    ]
