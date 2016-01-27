from django.conf.urls.defaults import include, patterns, url


urlpatterns = patterns('',
    url(r'^', include('posts.urls')),
)
