# Generated by Django 4.0.4 on 2022-06-02 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0006_rename_available_book_is_available'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/%Y/%m/%d'),
        ),
    ]