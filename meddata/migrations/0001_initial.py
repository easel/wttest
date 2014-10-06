# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drug',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('license_title', models.CharField(max_length=200)),
                ('mantainer', models.CharField(max_length=200)),
                ('private', models.BooleanField()),
                ('maintainer_email', models.EmailField(max_length=75)),
                ('num_tags', models.IntegerField(default=0)),
                ('drug_id', models.CharField(max_length=200)),
                ('metadata_created', models.DateTimeField()),
                ('license', models.CharField(max_length=200)),
                ('metadata_modified', models.DateTimeField()),
                ('author', models.CharField(max_length=200)),
                ('author_email', models.EmailField(max_length=75)),
                ('state', models.CharField(max_length=200)),
                ('version', models.IntegerField()),
                ('license_id', models.CharField(max_length=200)),
                ('drug_type', models.CharField(max_length=200)),
                ('num_resources', models.IntegerField(default=0)),
                ('organization', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('isopen', models.BooleanField()),
                ('notes_rendered', models.TextField()),
                ('url', models.URLField()),
                ('ckan_url', models.URLField()),
                ('notes', models.TextField()),
                ('owner_org', models.CharField(max_length=200)),
                ('ratings_average', models.IntegerField()),
                ('ratings_count', models.IntegerField(default=0)),
                ('title', models.CharField(max_length=200)),
                ('revision_id', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Drug_Tracking_Summary',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('total', models.IntegerField(default=0)),
                ('recent', models.IntegerField(default=0)),
                ('drug', models.ForeignKey(to='meddata.Drug')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Extras',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('coverage_period_start', models.DateTimeField()),
                ('unit_of_analysis', models.CharField(max_length=200)),
                ('hd2_workflow_id', models.IntegerField()),
                ('agency', models.CharField(max_length=200)),
                ('bureau_code', models.CharField(max_length=200)),
                ('geographic_granularity', models.CharField(max_length=200)),
                ('technical_documentation', models.URLField()),
                ('collection_frequency', models.CharField(max_length=200)),
                ('agency_program_url', models.URLField()),
                ('date_updated', models.DateTimeField()),
                ('date_released', models.DateTimeField()),
                ('author_id', models.URLField()),
                ('migration_notes_JSON', models.TextField()),
                ('subject_area_1', models.CharField(max_length=200)),
                ('drug', models.ForeignKey(to='meddata.Drug')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('drug', models.ForeignKey(to='meddata.Drug')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('drug', models.ForeignKey(to='meddata.Drug')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('resource_group_id', models.CharField(max_length=200)),
                ('cache_last_updated', models.DateTimeField()),
                ('package_id', models.CharField(max_length=200)),
                ('webstore_last_updated', models.DateTimeField()),
                ('resource_id', models.CharField(max_length=200)),
                ('size', models.CharField(max_length=200)),
                ('last_modified', models.DateTimeField()),
                ('resource_hash', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('format', models.CharField(max_length=200)),
                ('mimetype_inner', models.CharField(max_length=200)),
                ('mimetype', models.CharField(max_length=200)),
                ('cache_url', models.URLField()),
                ('name', models.CharField(max_length=200)),
                ('created', models.DateTimeField()),
                ('url', models.URLField()),
                ('webstore_url', models.URLField()),
                ('position', models.IntegerField(default=0)),
                ('resource_type', models.CharField(max_length=200)),
                ('drug', models.ForeignKey(to='meddata.Drug')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Resource_Tracking_Summary',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('total', models.IntegerField(default=0)),
                ('recent', models.IntegerField(default=0)),
                ('resource', models.ForeignKey(to='meddata.Resource')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('drug', models.ForeignKey(to='meddata.Drug')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
