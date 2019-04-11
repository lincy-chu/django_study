# Generated by Django 2.2 on 2019-04-11 13:38

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20190411_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='id',
            field=models.CharField(default=uuid.UUID('05529469-5c1c-11e9-abab-509a4c2c7107'), max_length=32, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='host',
            name='id',
            field=models.CharField(default=uuid.UUID('05529468-5c1c-11e9-a922-509a4c2c7107'), max_length=32, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='user_info',
            name='id',
            field=models.CharField(default=uuid.UUID('0552465e-5c1c-11e9-9f5b-509a4c2c7107'), max_length=32, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='usergroup',
            name='id',
            field=models.CharField(default=uuid.UUID('05526d5c-5c1c-11e9-8d69-509a4c2c7107'), max_length=32, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='id',
            field=models.CharField(default=uuid.UUID('0552465f-5c1c-11e9-aaa4-509a4c2c7107'), max_length=32, primary_key=True, serialize=False, unique=True),
        ),
    ]