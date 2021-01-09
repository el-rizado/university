# Generated by Django 3.1 on 2021-01-09 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0005_auto_20210109_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='time',
            name='end_time',
            field=models.CharField(choices=[('09:00', '09:00'), ('15:30', '15:30'), ('12:00', '12:00'), ('10:30', '10:30'), ('17:30', '17:30')], default='09:00', max_length=5),
        ),
        migrations.AlterField(
            model_name='time',
            name='start_time',
            field=models.CharField(choices=[('09:00', '09:00'), ('14:00', '14:00'), ('10:30', '10:30'), ('16:00', '16:00'), ('07:30', '07:30')], default='07:30', max_length=5),
        ),
    ]
