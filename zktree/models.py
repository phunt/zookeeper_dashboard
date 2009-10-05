from django.conf import settings

from datetime import datetime
import threading
import zookeeper

zookeeper.set_log_stream(open("cli_log.txt","w"))

TIMEOUT = 10.0

class ZKClient(object):
    def __init__(self, servers, timeout):
        self.connected = False
        self.conn_cv = threading.Condition( )
        self.handle = -1

        self.conn_cv.acquire()
        print("Connecting to %s" % (servers))
        self.handle = zookeeper.init(servers, self.connection_watcher, 30000)
        self.conn_cv.wait(timeout)
        self.conn_cv.release()

        if not self.connected:
            raise Error("Unable to connect to %s" % (servers))

        print("Connected, handle is %d" % (self.handle))

    def connection_watcher(self, h, type, state, path):
        self.handle = h
        self.conn_cv.acquire()
        self.connected = True
        self.conn_cv.notifyAll()
        self.conn_cv.release()

    def close(self):
        zookeeper.close(self.handle)
    
    def get(self, path, watcher=None):
        return zookeeper.get(self.handle, path, watcher)

    def get_children(self, path, watcher=None):
        return zookeeper.get_children(self.handle, path, watcher)

ZOOKEEPER_SERVERS = getattr(settings,'ZOOKEEPER_SERVERS')

class ZNode(object):
    def __init__(self, path="/"):
        self.path = path
        zk = ZKClient(ZOOKEEPER_SERVERS, TIMEOUT)
        try:
            self.data, self.stat = zk.get(path)
            self.stat['ctime'] = datetime.fromtimestamp(self.stat['ctime']/1000)
            self.stat['mtime'] = datetime.fromtimestamp(self.stat['mtime']/1000)
            self.children = zk.get_children(path) or []
        finally:
            zk.close()
