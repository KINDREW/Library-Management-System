# Generated by Django 4.0.4 on 2022-06-02 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentications', '0008_alter_users_options_alter_users_email_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='username',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
    ]
