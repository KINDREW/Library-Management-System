# Generated by Django 4.0.4 on 2022-05-19 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentications', '0002_alter_users_options_rename_name_users_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='Email_Address',
            field=models.EmailField(blank=True, default=None, max_length=200, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='users',
            name='username',
            field=models.CharField(blank=True, max_length=200, unique=True),
        ),
    ]
