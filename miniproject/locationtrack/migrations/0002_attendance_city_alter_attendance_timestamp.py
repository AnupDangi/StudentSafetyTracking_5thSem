# Generated by Django 5.1.4 on 2024-12-10 10:30

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locationtrack', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='city',
            field=models.CharField(blank=True, default='Unknown', max_length=100),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.localtime),
        ),
    ]
