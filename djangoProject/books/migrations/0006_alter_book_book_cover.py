# Generated by Django 5.0.3 on 2024-03-12 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_remove_book_image_path_book_book_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_cover',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]