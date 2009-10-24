from django.shortcuts import render_to_response
import string

from zookeeper_dashboard.zktree.models import ZNode

def istext(s, text_chars="".join(map(chr, range(32, 127))) + "\n\r\t\b"):
    if "\0" in s: return False
    if not s: return True
    t = s.translate(string.maketrans("", ""), text_chars)
    return len(t) == 0

def index(request, path=""):
    print(path)
    path = "/" + path
    try:
        znode = ZNode(path)
        znode.children.sort()
        if not istext(znode.data):
            znode.data = "0x" + "".join(["%d" % (ord(d)) for d in znode.data])
            znode.datatype = "bin"
        else:
            znode.datatype = "str"

        return render_to_response('zktree/index.html',
                                  {'znode':znode})
    except Exception as err:
        return render_to_response('zktree/error.html',
                                  {'error':str(err)})
