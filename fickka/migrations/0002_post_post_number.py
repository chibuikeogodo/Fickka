# Generated by Django 3.0.10 on 2021-05-03 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fickka', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_number',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]