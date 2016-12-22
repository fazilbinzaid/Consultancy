# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import recruits.managers
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(help_text='Designates that this user has all permissions without explicitly assigning them.', default=False, verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=50)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_query_name='user', related_name='user_set', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_query_name='user', related_name='user_set', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name_plural': 'users',
                'verbose_name': 'user',
            },
            managers=[
                ('objects', recruits.managers.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('location', models.CharField(max_length=20)),
                ('current_ctc', models.DecimalField(max_digits=3, decimal_places=2)),
                ('expected_ctc', models.DecimalField(max_digits=3, decimal_places=2)),
                ('notice_period', models.IntegerField()),
                ('resume', models.FileField(blank=True, upload_to='docs/')),
                ('recording', models.FileField(blank=True, upload_to='media/')),
                ('recording_optional', models.FileField(blank=True, upload_to='')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='profiles')),
            ],
        ),
        migrations.CreateModel(
            name='Skillset',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('skill', models.CharField(max_length=10)),
                ('exp', models.IntegerField()),
                ('profile', models.ForeignKey(to='recruits.Profile', related_name='skills')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='skillset',
            unique_together=set([('profile', 'skill', 'exp')]),
        ),
    ]
