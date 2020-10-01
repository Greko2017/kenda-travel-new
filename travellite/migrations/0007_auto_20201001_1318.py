# Generated by Django 2.2.4 on 2020-10-01 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travellite', '0006_history_booking_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='bookingStatus',
            field=models.CharField(choices=[('pending', 'En Cours'), ('rejected', 'Rejeté'), ('invoiced', 'Approuvé')], default='pending'),
        ),
    ]
