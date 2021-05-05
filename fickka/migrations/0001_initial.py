# Generated by Django 3.0.10 on 2021-05-05 08:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('date', models.DateTimeField(auto_now=True)),
                ('image_1', models.ImageField(blank=True, default=None, null=True, upload_to='')),
                ('image_2', models.ImageField(blank=True, default=None, null=True, upload_to='')),
                ('image_3', models.ImageField(blank=True, default=None, null=True, upload_to='')),
                ('To_homepage', models.BooleanField(default=False)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('post_title', models.CharField(blank=True, max_length=100, null=True)),
                ('views', models.IntegerField(blank=True, default=0, null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('slug', models.SlugField()),
                ('post_number', models.IntegerField(blank=True, default=0, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fickka.Category')),
                ('likes', models.ManyToManyField(blank=True, default=None, null=True, related_name='blog_post', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('threads', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('image_1', models.ImageField(blank=True, default=None, null=True, upload_to='')),
                ('image_2', models.ImageField(blank=True, default=None, null=True, upload_to='')),
                ('image_3', models.ImageField(blank=True, default=None, null=True, upload_to='')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='thread', to='fickka.Post')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Biography', models.TextField(max_length=100)),
                ('Gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=50)),
                ('State', models.CharField(max_length=20)),
                ('Occupation', models.CharField(choices=[('Student', 'Student'), ('Employed', 'Employed'), ('Self Employed', 'Self Employed'), ('Unemployed', 'Unemployed')], max_length=30)),
                ('Contact', models.IntegerField(blank=True, null=True)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='images/profile')),
                ('fb_url', models.CharField(blank=True, max_length=255, null=True)),
                ('twitter_url', models.CharField(blank=True, max_length=255, null=True)),
                ('instagram_url', models.CharField(blank=True, max_length=255, null=True)),
                ('confirmed', models.BooleanField(blank=True, default=False, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('likes', models.ManyToManyField(blank=True, related_name='comment_like', to=settings.AUTH_USER_MODEL)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='fickka.Comment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='fickka.Post')),
            ],
        ),
    ]
