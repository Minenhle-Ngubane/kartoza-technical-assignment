# Generated by Django 3.2.6 on 2021-10-02 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_alter_userprofile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='address_is_valid',
            field=models.BooleanField(default=False),
        ),
    ]