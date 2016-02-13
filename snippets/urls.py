# coding=utf-8
# snippets/urls.py
from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns

from snippets import views


# API 路径
urlpatterns = format_suffix_patterns(patterns('snippets.views',
    url(r'^$', 'api_root'),
    url(r'^snippets/$',
        views.SnippetList.as_view(),
        name='snippet-list'),
    url(r'^snippets/(?P<pk>[0-9]+)/$',
        views.SnippetDetail.as_view(),
        name='snippet-detail'),
    url(r'^snippets/(?P<pk>[0-9]+)/highlight/$',
        views.SnippetHighlight.as_view(),
        name='snippet-highlight'),
    url(r'^users/$',
        views.UserList.as_view(),
        name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$',
        views.UserDetail.as_view(),
        name='user-detail')
))

# 可浏览式登录API
urlpatterns += patterns('',
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
)