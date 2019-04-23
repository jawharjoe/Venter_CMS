# Generated by Django 2.1.2 on 2019-01-28 06:13

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Category',
            },
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('csv_file', models.FileField(upload_to='Organisation/CSV File/%Y/%m/%d/')),
                ('uploaded_date', models.DateTimeField(default=datetime.datetime.now)),
                ('file_size', models.IntegerField(blank=True)),
                ('file_name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'CSV File Meta',
            },
        ),
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Headers',
            },
        ),
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('organisation_name', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('organisation_logo', models.ImageField(blank=True, null=True, upload_to='Organisation/Organisation Logo/%Y/%m/%d/', verbose_name='Organisation Logo')),
                ('additional_details', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='Organisation/Employee Profile Picture/%Y/%m/%d/', verbose_name='Employee Profile picture')),
                ('phone_number', models.CharField(blank=True, max_length=10)),
                ('organisation_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Venter.Organisation')),
            ],
        ),
        migrations.AddField(
            model_name='header',
            name='organisation_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Venter.Organisation'),
        ),
        migrations.AddField(
            model_name='file',
            name='uploaded_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='category',
            name='organisation_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Venter.Organisation'),
        ),
    ]
