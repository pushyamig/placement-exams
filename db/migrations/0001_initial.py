# Generated by Django 3.0.6 on 2020-06-10 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Exam ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Exam Name')),
                ('sa_code', models.CharField(max_length=5, unique=True, verbose_name='Exam SA Code')),
                ('course_id', models.IntegerField(unique=True, verbose_name='Canvas Course ID for Exam')),
                ('assignment_id', models.IntegerField(unique=True, verbose_name='Canvas Assignment ID for Exam')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='Report ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Report Name')),
                ('contact', models.CharField(max_length=100, verbose_name='Report Contact Email')),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Submission ID')),
                ('submission_id', models.IntegerField(unique=True, verbose_name='Canvas Submission ID')),
                ('student_uniqname', models.CharField(max_length=50, verbose_name='Student Uniqname')),
                ('submitted_timestamp', models.DateField(verbose_name='Submitted At Date & Time')),
                ('score', models.FloatField(verbose_name='Submission Score')),
                ('transmitted', models.BooleanField(verbose_name='Transmitted')),
                ('transmitted_timestamp', models.DateField(verbose_name='Transmitted At Date & Time')),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submissions', to='db.Exam')),
            ],
        ),
        migrations.AddField(
            model_name='exam',
            name='report',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exams', to='db.Report'),
        ),
    ]
