from django.conf.urls import patterns, include, url

from views import PostListView, PostDetailView


urlpatterns = patterns('',
    url(r'^$', PostListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', PostDetailView.as_view(), name='detail'),
)
