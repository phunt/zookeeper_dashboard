from django.shortcuts import render_to_response

from zookeeper_dashboard.zktree.models import ZNode

def index(request, path=""):
    print(path)
    path = "/" + path
    try:
        znode = ZNode(path)
        znode.children.sort()
        return render_to_response('zktree/index.html',
                                  {'znode':znode})
    except Exception as err:
        return render_to_response('zktree/error.html',
                                  {'error':str(err)})
