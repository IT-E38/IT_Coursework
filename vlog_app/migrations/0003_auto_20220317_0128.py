# Generated by Django 2.1.5 on 2022-03-17 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vlog_app', '0002_auto_20220315_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='dob',
            field=models.DateField(),
        ),
    ]
