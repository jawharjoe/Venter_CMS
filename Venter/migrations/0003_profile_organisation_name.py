# Generated by Django 2.1.2 on 2019-01-08 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Venter', '0002_auto_20190108_1809'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='organisation_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Venter.Organisation'),
        ),
    ]
