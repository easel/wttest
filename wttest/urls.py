from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.models import User
from meddata.models import Drug
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

class DrugSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Drug
		fields = ('id', 'name', 'author', 'metadata_created', 'metadata_modified')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DrugViewSet(viewsets.ModelViewSet):
	queryset = Drug.objects.all()
	serializer_class = DrugSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'drugs', DrugViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wttest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'', include('social_auth.urls')),
    url(r'^meddata/', include('meddata.urls')),
)
