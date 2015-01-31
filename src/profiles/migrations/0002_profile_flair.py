# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='flair',
            field=models.CharField(null=True, verbose_name='Flair', blank=True, max_length=200),
            preserve_default=True,
        ),
    ]
