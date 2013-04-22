from django.conf.urls import patterns, url

from views import PostListView, PostDetailView


urlpatterns = patterns('',
    url(r'^$', PostListView.as_view(), name='list'),
    url(r'^(?P<pk>[\d]+)/$', PostDetailView.as_view(), name='detail'),
    url(r'^(?P<slug>[-\w]+)/$', PostDetailView.as_view(), name='detail-by-slug'),
)
