# Generated by Django 5.0.6 on 2024-12-22 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_post_views'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='slug_fiedl',
            new_name='slug',
        ),
    ]
