# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(serialize=False, primary_key=True, to=settings.AUTH_USER_MODEL)),
                ('slug', models.SlugField(unique=True, max_length=32, editable=False, blank=True)),
                ('picture', models.ImageField(verbose_name='Profile picture', upload_to='profile_pics/%Y-%m-%d/', blank=True, null=True)),
                ('bio', models.CharField(verbose_name='Short Bio', max_length=200, blank=True, null=True)),
                ('email_verified', models.BooleanField(default=False, verbose_name='Email verified')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
