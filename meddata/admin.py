from django.contrib import admin
from meddata.models import Drug
from meddata.models import Resource
from meddata.models import Tag
from meddata.models import Relationship
from meddata.models import Group
from meddata.models import Drug_Tracking_Summary
from meddata.models import Resource_Tracking_Summary
from meddata.models import Extras

class DrugAdmin(admin.ModelAdmin):
	list_display = ('name', 'author', 'metadata_created', 'metadata_modified')
	list_filter = ['metadata_created', 'metadata_modified']
	search_fields = ['name', 'author']

# Register your models here.
admin.site.register(Drug, DrugAdmin)
admin.site.register(Resource)
admin.site.register(Tag)
admin.site.register(Relationship)
admin.site.register(Group)
admin.site.register(Drug_Tracking_Summary)
admin.site.register(Resource_Tracking_Summary)
admin.site.register(Extras)