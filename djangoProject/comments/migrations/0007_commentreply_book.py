# Generated by Django 5.0.3 on 2024-04-05 08:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_delete_comment'),
        ('comments', '0006_remove_commentreply_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentreply',
            name='book',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='books.book'),
        ),
    ]
