# Generated by Django 4.0.4 on 2022-06-02 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentications', '0012_alter_users_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='username',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
