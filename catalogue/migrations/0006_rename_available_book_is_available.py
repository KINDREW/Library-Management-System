# Generated by Django 4.0.4 on 2022-06-02 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0005_alter_category_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='available',
            new_name='is_available',
        ),
    ]
