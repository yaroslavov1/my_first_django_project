# Generated by Django 5.0.3 on 2024-03-22 18:58

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_reply'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Reply',
            new_name='ReplyComment',
        ),
        migrations.AlterModelOptions(
            name='replycomment',
            options={},
        ),
    ]
