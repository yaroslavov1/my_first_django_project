# Generated by Django 5.0.3 on 2024-03-12 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_profile_is_staff_alter_profile_avatar'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='is_staff',
            new_name='is_moderator',
        ),
    ]
