# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2022-06-08 20:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_content', models.TextField(max_length=2000)),
                ('media', models.FileField(blank=True, null=True, upload_to='post_files')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('post_status', models.CharField(choices=[('1', 'publish'), ('2', 'draft')], max_length=7)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Profile')),
                ('dislikes', models.ManyToManyField(blank=True, related_name='post_dislikes', to='users.Profile')),
                ('likes', models.ManyToManyField(blank=True, related_name='post_likes', to='users.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='PostComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('comment_content', models.TextField(max_length=500)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Profile')),
                ('dislikes', models.ManyToManyField(blank=True, related_name='comment_dislikes', to='users.Profile')),
                ('likes', models.ManyToManyField(blank=True, related_name='comment_likes', to='users.Profile')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='social_app.Post')),
            ],
        ),
    ]
