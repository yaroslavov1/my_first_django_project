# Generated by Django 5.0.3 on 2024-03-12 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_alter_book_uploaded_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='book_cover',
        ),
        migrations.AddField(
            model_name='book',
            name='image_path',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
