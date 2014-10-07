# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meddata', '0004_auto_20141007_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drug',
            name='metadata_modified',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='drug',
            name='ratings_average',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='extras',
            name='coverage_period_start',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='extras',
            name='date_released',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='extras',
            name='date_updated',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='resource',
            name='cache_last_updated',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='resource',
            name='last_modified',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='resource',
            name='webstore_last_updated',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
