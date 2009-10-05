from django.shortcuts import render_to_response

from zookeeper_dashboard.zktree.models import ZNode

def index(request, path=""):
    print(path)
    path = "/" + path
    znode = ZNode(path)
    znode.children.sort()
    return render_to_response('zktree/index.html',
                              {'znode':znode})
