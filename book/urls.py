

from django.conf.urls import url, include
from django.contrib import admin


from .views import index,booklist,intex,post,post_json,get_headers,sessions

urlpatterns = [
    url(r'^index/$',index),
    url(r'^booklist/$',booklist,name='test'),
    url(r'^(?P<value1>\d+)/(?P<value2>\d+)/$',intex),
    url(r'^(?P<value1>)\w+/(?P<value2>\w+)/$',post),
    url(r'^post_json/$',post_json),
    url(r'^get_header/$',get_headers),
    url(r'^sessions/$', sessions),

]
