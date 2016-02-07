# from django.conf.urls import patterns, include, url
# 
# from django.contrib import admin
# admin.autodiscover()
# 
# urlpatterns = patterns('',
#     # Examples:
#     # url(r'^$', 'tutorial.views.home', name='home'),
#     # url(r'^blog/', include('blog.urls')),
# 
#     url(r'^admin/', include(admin.site.urls)),
#     url(r'^', include('snippets.urls')),
# )




from rest_framework import routers
from django.conf.urls import patterns, url, include
from quickstart import views
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
#     url(r'^', include('snippets.urls')),
)