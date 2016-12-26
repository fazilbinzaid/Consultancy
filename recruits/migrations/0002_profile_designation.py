# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recruits', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='designation',
            field=models.CharField(max_length=20, choices=[('Project Manager', 'Project Manager'), ('Developer', 'Developer'), ('Tester', 'Tester'), ('Technical Lead', 'Technical Lead'), ('Hybrid', 'Hybrid'), ('DevOps', 'DevOps'), ('Fresher', 'Fresher'), ('Project Coordinator', 'Project Coordinator'), ('UI/UX Designer', 'UI/UX Designer'), ('UI/UX Developer', 'UI/UX Developer'), ('HTML Developer', 'HTML Developer')], default='Developer'),
            preserve_default=False,
        ),
    ]
