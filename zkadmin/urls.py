from django.conf.urls.defaults import *

urlpatterns = patterns('zookeeper_web_console.zkadmin.views',
    (r'^$','index'), 
)
