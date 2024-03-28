# Generated by Django 5.0.3 on 2024-03-12 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_remove_book_book_cover_book_image_path'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='image_path',
        ),
        migrations.AddField(
            model_name='book',
            name='book_cover',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
