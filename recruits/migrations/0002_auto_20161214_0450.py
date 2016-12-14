# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recruits', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='interview',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='resume',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
