# Generated by Django 4.2.4 on 2023-10-05 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_user_verify_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='verify_token',
            field=models.CharField(default='114e30bc2a2f'),
        ),
    ]