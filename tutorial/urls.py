# coding=utf-8
from django.conf.urls import patterns, url, include
from snippets import views
from rest_framework.routers import DefaultRouter

# 创建router并注册viewset.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# router会自动生成url
# 我们只需要额外提供可浏览性登入API
urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)