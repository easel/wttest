# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meddata', '0002_auto_20141006_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drug',
            name='version',
            field=models.CharField(max_length=200),
        ),
    ]
