from django.db import models

# Create your models here.

class Drug(models.Model):
	license_title = models.CharField(max_length=200)
	mantainer = models.CharField(max_length=200)
	private = models.BooleanField(default='false')
	maintainer_email = models.EmailField(max_length=75)
	num_tags = models.IntegerField(default=0)
	drug_id = models.CharField(max_length=200)
	metadata_created = models.DateTimeField()
	license = models.CharField(max_length=200)
	metadata_modified = models.DateTimeField(null=True, blank=True)
	author = models.CharField(max_length=200)
	author_email = models.EmailField(max_length=75)
	state = models.CharField(max_length=200)
	version = models.CharField(max_length=200)
	license_id = models.CharField(max_length=200)
	drug_type = models.CharField(max_length=200)
	num_resources = models.IntegerField(default=0)
	organization = models.CharField(max_length=200)
	name = models.CharField(max_length=200)
	isopen = models.BooleanField(default='false')
	notes_rendered = models.TextField()
	url = models.URLField(max_length=200)
	ckan_url = models.URLField(max_length=200)
	notes = models.TextField()
	owner_org = models.CharField(max_length=200)
	ratings_average = models.IntegerField(null=True, blank=True)
	ratings_count = models.IntegerField(default=0)
	title = models.CharField(max_length=200)
	revision_id = models.CharField(max_length=200)


class Resource(models.Model):
	drug = models.ForeignKey(Drug)
	resource_group_id = models.CharField(max_length=200)
	cache_last_updated = models.DateTimeField(null=True, blank=True)
	package_id = models.CharField(max_length=200)
	webstore_last_updated = models.DateTimeField(null=True, blank=True)
	resource_id = models.CharField(max_length=200)
	size = models.CharField(max_length=200)
	last_modified = models.DateTimeField(null=True, blank=True)
	resource_hash = models.CharField(max_length=200)
	description = models.CharField(max_length=200)
	format = models.CharField(max_length=200)
	mimetype_inner = models.CharField(max_length=200)
	mimetype = models.CharField(max_length=200)
	cache_url = models.URLField(max_length=200)
	name = models.CharField(max_length=200)
	created = models.DateTimeField()
	url = models.URLField(max_length=200)
	webstore_url = models.URLField(max_length=200)
	position = models.IntegerField(default=0)
	resource_type = models.CharField(max_length=200)

class Tag(models.Model):
	drug = models.ForeignKey(Drug)
	name = models.CharField(max_length=200)

class Relationship(models.Model):
	drug = models.ForeignKey(Drug)
	name = models.CharField(max_length=200)

class Group(models.Model):
	drug = models.ForeignKey(Drug)
	name = models.CharField(max_length=200)

class Drug_Tracking_Summary(models.Model):
	drug = models.ForeignKey(Drug)
	total = models.IntegerField(default=0)
	recent = models.IntegerField(default=0)

class Resource_Tracking_Summary(models.Model):
	resource = models.ForeignKey(Resource)
	total = models.IntegerField(default=0)
	recent = models.IntegerField(default=0)

class Extras(models.Model):
	drug = models.ForeignKey(Drug)
	coverage_period_start = models.DateTimeField(null=True, blank=True)
	unit_of_analysis = models.CharField(max_length=200)
	hd2_workflow_id = models.IntegerField()
	agency = models.CharField(max_length=200)
	bureau_code = models.CharField(max_length=200)
	geographic_granularity = models.CharField(max_length=200)
	technical_documentation = models.URLField(max_length=200)
	collection_frequency = models.CharField(max_length=200)
	agency_program_url = models.URLField(max_length=200)
	date_updated = models.DateTimeField(null=True, blank=True)
	date_released = models.DateTimeField(null=True, blank=True)
	author_id = models.URLField(max_length=200)
	migration_notes_JSON = models.TextField()
	subject_area_1 = models.CharField(max_length=200)