# Generated by Django 2.2.12 on 2021-01-09 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memories_app', '0006_auto_20210109_1022'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='lngLat',
        ),
        migrations.AddField(
            model_name='post',
            name='latitude',
            field=models.FloatField(blank=True, default=56.5, max_length=10, null=True),
        ),
    ]