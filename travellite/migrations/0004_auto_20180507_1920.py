# Generated by Django 2.0.4 on 2018-05-07 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travellite', '0003_remove_hotel_startdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='companyName',
            field=models.CharField(default='company', max_length=30),
        ),
        migrations.AddField(
            model_name='history',
            name='location',
            field=models.CharField(default='location', max_length=30),
        ),
    ]
