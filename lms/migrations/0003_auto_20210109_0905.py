# Generated by Django 3.1 on 2021-01-09 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0002_auto_20210109_0840'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='time',
            name='end_time',
            field=models.CharField(choices=[('15:30', '15:30'), ('10:30', '10:30'), ('17:30', '17:30'), ('09:00', '09:00'), ('12:00', '12:00')], default='09:00', max_length=5),
        ),
        migrations.AlterField(
            model_name='time',
            name='start_time',
            field=models.CharField(choices=[('10:30', '10:30'), ('16:00', '16:00'), ('09:00', '09:00'), ('14:00', '14:00'), ('07:30', '07:30')], default='07:30', max_length=5),
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.IntegerField()),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='lms.faculty')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='lms.day')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='lms.room')),
                ('time', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='lms.time')),
            ],
        ),
    ]
