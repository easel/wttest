# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meddata', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drug',
            name='isopen',
            field=models.BooleanField(default=b'false'),
        ),
        migrations.AlterField(
            model_name='drug',
            name='private',
            field=models.BooleanField(default=b'false'),
        ),
    ]
