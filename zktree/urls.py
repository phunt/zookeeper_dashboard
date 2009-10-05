from django.conf.urls.defaults import *

urlpatterns = patterns('zookeeper_dashboard.zktree.views',
    (r'^$','index'), 
)
