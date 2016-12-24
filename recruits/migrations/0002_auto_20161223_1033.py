# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recruits', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='skillset',
            unique_together=set([('profile', 'skill')]),
        ),
    ]
