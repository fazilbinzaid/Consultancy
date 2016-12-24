# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import recruits.managers


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(help_text='Designates that this user has all permissions without explicitly assigning them.', default=False, verbose_name='superuser status')),
                ('email', models.EmailField(unique=True, max_length=254)),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=50)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', blank=True, to='auth.Group', related_query_name='user', verbose_name='groups', related_name='user_set')),
                ('user_permissions', models.ManyToManyField(help_text='Specific permissions for this user.', blank=True, to='auth.Permission', related_query_name='user', verbose_name='user permissions', related_name='user_set')),
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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('location', models.CharField(max_length=20)),
                ('current_ctc', models.DecimalField(decimal_places=2, max_digits=3)),
                ('expected_ctc', models.DecimalField(decimal_places=2, max_digits=3)),
                ('notice_period', models.IntegerField()),
                ('resume', models.FileField(upload_to='docs/', blank=True)),
                ('recording', models.FileField(upload_to='media/', blank=True)),
                ('recording_optional', models.FileField(upload_to='', blank=True)),
                ('user', models.ForeignKey(related_name='profiles', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Skillset',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('skill', models.CharField(max_length=10)),
                ('exp', models.IntegerField()),
                ('profile', models.ForeignKey(related_name='skills', to='recruits.Profile')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='skillset',
            unique_together=set([('profile', 'skill', 'exp')]),
        ),
    ]
