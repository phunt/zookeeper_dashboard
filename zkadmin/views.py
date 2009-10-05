from django.shortcuts import render_to_response
from django.conf import settings

from zookeeper_dashboard.zkadmin.models import ZKServer

ZOOKEEPER_SERVERS = getattr(settings,'ZOOKEEPER_SERVERS').split(',')

def index(request):
    server_data = []
    for i, server in enumerate(ZOOKEEPER_SERVERS):
        zkserver = ZKServer(server)
        zkserver.id = i
        server_data.append(zkserver)

    return render_to_response('zkadmin/index.html',
                              {'ZOOKEEPER_SERVERS':ZOOKEEPER_SERVERS,
                               'server_data':server_data})

def detail(request, server_id):
    server_data = ZKServer(ZOOKEEPER_SERVERS[int(server_id)])
    server_data.id = server_id
    return render_to_response('zkadmin/detail.html',
                              {'server_data':server_data})
