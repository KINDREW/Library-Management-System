# Generated by Django 4.0.4 on 2022-05-19 22:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentications', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='users',
            options={'ordering': ('username',)},
        ),
        migrations.RenameField(
            model_name='users',
            old_name='name',
            new_name='username',
        ),
    ]