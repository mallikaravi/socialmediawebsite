# Generated by Django 3.2.6 on 2022-06-12 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social_app', '0007_auto_20220612_1638'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='post_content',
            new_name='content',
        ),
    ]
