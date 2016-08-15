# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-08-04 05:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import quiz.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date', models.DateTimeField(auto_now=True, verbose_name='last edit')),
                ('uploader', models.CharField(max_length=50)),
                ('rate', models.IntegerField(default=0, validators=[quiz.models.Question.valid_rate])),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('url_slug', models.SlugField(allow_unicode=True, null=True)),
                ('publish_date', models.DateTimeField(null=True, verbose_name='date submitted')),
                ('draft_date', models.DateTimeField(null=True, verbose_name='date drafted')),
                ('pubdr', models.CharField(choices=[('Publish', 'انتشار'), ('Draft', 'چرک نویس')], default='Publish', max_length=20)),
                ('type', models.CharField(choices=[('Multi', 'چند گزینه ای'), ('Descriptive', 'تشریحی'), ('Blank', 'جای خالی'), ('TrueFlase', 'صحیح غلط')], default='Descriptive', max_length=20)),
                ('rate', models.IntegerField(default=0, validators=[quiz.models.Question.valid_rate])),
                ('difficulty', models.IntegerField(default=0, validators=[quiz.models.Question.valid_rate])),
                ('lesson', models.CharField(max_length=50, validators=[quiz.models.Question.valid_lessons])),
                ('user', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ('-publish_date',),
            },
        ),
        migrations.AddField(
            model_name='answer',
            name='related_question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Question'),
        ),
    ]