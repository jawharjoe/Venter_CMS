# Generated by Django 2.1.2 on 2019-03-07 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Venter', '0024_auto_20190307_1555'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='file',
            options={'ordering': ['-uploaded_date'], 'verbose_name_plural': 'File'},
        ),
    ]
