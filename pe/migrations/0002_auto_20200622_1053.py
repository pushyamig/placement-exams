# Generated by Django 3.0.7 on 2020-06-22 14:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='default_time_filter',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 1, 0, 0, tzinfo=utc), verbose_name='Earliest Date & Time for Submission Search'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='submission',
            name='graded_timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 1, 0, 0, tzinfo=utc), verbose_name='Graded At Date & Time'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='report',
            name='contact',
            field=models.CharField(max_length=255, verbose_name='Report Contact Email'),
        ),
        migrations.AlterField(
            model_name='submission',
            name='student_uniqname',
            field=models.CharField(max_length=255, verbose_name='Student Uniqname'),
        ),
        migrations.AlterField(
            model_name='submission',
            name='transmitted_timestamp',
            field=models.DateTimeField(default=None, null=True, verbose_name='Transmitted At Date & Time'),
        ),
    ]