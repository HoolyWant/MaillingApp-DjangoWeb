# Generated by Django 4.2.4 on 2023-10-05 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_user_verify_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='verify_token',
            field=models.CharField(default='1e30ca43cdfe'),
        ),
    ]