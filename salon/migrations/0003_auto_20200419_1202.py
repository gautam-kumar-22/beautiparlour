# Generated by Django 2.1 on 2020-04-19 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salon', '0002_auto_20200418_2248'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactus',
            name='website',
        ),
        migrations.AddField(
            model_name='contactus',
            name='address',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='contactus',
            name='phone_number',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
