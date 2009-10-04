from django.shortcuts import render_to_response
from django.conf import settings
import zookeeper

ZOOKEEPER_SERVERS = getattr(settings,'ZOOKEEPER_SERVERS')

def index(request):
    return render_to_response('zkadmin/index.html',
                              {'ZOOKEEPER_SERVERS':ZOOKEEPER_SERVERS})
