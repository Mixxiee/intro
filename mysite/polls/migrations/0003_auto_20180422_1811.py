# Generated by Django 2.0.4 on 2018-04-22 16:11

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0002_p_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='P_USER',
            new_name='PUser',
        ),
    ]
