# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meddata', '0003_auto_20141007_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drug',
            name='ratings_average',
            field=models.CharField(max_length=200),
        ),
    ]
