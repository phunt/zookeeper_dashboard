from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('zookeeper_web_console',
    # Example:
    # (r'^zookeeper_web_console/', include('zookeeper_web_console.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/(.*)', admin.site.root),

    (r'^cluster/', include('zookeeper_web_console.zkadmin.urls')),
    (r'^tree/', include('zookeeper_web_console.zktree.urls')),
)
