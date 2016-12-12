# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consultancy',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('address', models.TextField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=10)),
                ('resume', models.FileField(upload_to='doc_uploads/', blank=True)),
                ('interview', models.FileField(upload_to='media_uploads/', blank=True)),
                ('consultancy', models.ForeignKey(to='recruits.Consultancy', related_name='profiles')),
            ],
        ),
        migrations.CreateModel(
            name='Skillset',
            fields=[
                ('skill', models.CharField(serialize=False, primary_key=True, max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='skillset',
            field=models.ManyToManyField(to='recruits.Skillset', related_name='skills'),
        ),
    ]
