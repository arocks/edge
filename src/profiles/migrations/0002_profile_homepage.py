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
            name='homepage',
            field=models.URLField(null=True, blank=True, verbose_name='Personal homepage'),
            preserve_default=True,
        ),
    ]
