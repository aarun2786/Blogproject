# Generated by Django 5.1.2 on 2024-12-01 16:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_post_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='bloger',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.bloger'),
        ),
    ]
