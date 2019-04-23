# Generated by Django 2.1.2 on 2019-02-01 13:31

import Venter.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Venter', '0006_auto_20190201_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organisation',
            name='organisation_logo',
            field=models.ImageField(blank=True, null=True, upload_to=Venter.models.get_organisation_logo_path, verbose_name='Organisation Logo'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to=Venter.models.get_user_profile_picture_path, verbose_name='Employee Profile picture'),
        ),
    ]
