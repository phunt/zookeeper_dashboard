h1. ZooKeeper Dashboard

*Author: "Patrick Hunt":http://people.apache.org/~phunt/* (follow me on "twitter":http://twitter.com/phunt)

h2. Summary

"This project":http://github.com/phunt/zookeeper_dashboard uses Django and the zkpython bindings to provide a dashboard for a ZooKeeper ensemble (cluster).

* Cluster summary
* Individual server detail
* Client connection detail
* Navigate & examine the live znode hierarchy

This is a work in progress. Want more? Ping me on "twitter":http://twitter.com/phunt or enter an "issue":http://github.com/phunt/zookeeper_dashboard/issues on GitHub.

h3. What's Apache ZooKeeper?

From the "official site":http://hadoop.apache.org/zookeeper/: "ZooKeeper is a high-performance coordination service for distributed applications."

It exposes common services - such as naming, configuration management, synchronization, and group services - in a simple interface so you don't have to write them from scratch. You can use it off-the-shelf to implement consensus, group management, leader election, and presence protocols.

h2. Overview

Django and the zkpython bindings are used to provide a dashboard for a ZooKeeper ensemble (cluster).

h2. License

This project is licensed under the Apache License Version 2.0

h2. Requirements

* Django 1.0+

h2. Usage

Edit settings.py. The top of the file has the ZOOKEEPER specific settings.

* ZOOKEEPER_SERVERS - host:port(,host:port)* of all servers in your cluster. This is the same information that you provide in your ZooKeeper client configuration.

then start the django server

<code>
PYTHONPATH=lib.linux-i686-2.6 LD_LIBRARY_PATH=lib.linux-i686-2.6 ./manage.py runserver
</code>

Obviously the dashboard needs access to the serving cluster (it queries the server's client port per ZOOKEEPER_SERVERS configuration).

Finally open a link in your browser to the server: "http://127.0.0.1:8000/":http://127.0.0.1:8000/

*Note*: you may need to compile the zookeeper python binding yourself, this project includes only 32bit linux binaries. Additionally, the django - zookeeper bridge relies on some changes to the zkpython binding that are not yet released, so if you do compile yourself you will need to compile zkpython from the Apache "ZooKeeper SVN trunk":http://hadoop.apache.org/zookeeper/version_control.html (this should be addressed as soon as ZooKeeper 3.3.0 is released).

ZooKeeper client output is written to "cli_log.txt".

h2. Limitations

ACLs are not yet fully supported. In particular the django server runs as an un-authenticated user. If nodes are protected by ACLs the server will not be able to access them.

h2. Screenshots

h3. Cluster Summary

<a href="http://www.flickr.com/photos/35605239@N00/4035924997/" title="dashboard_summary by phunt, on Flickr"><img src="http://farm3.static.flickr.com/2483/4035924997_f97e4901ef.jpg" width="500" height="226" alt="dashboard_summary" /></a>

h3. Server Summary

<a href="http://www.flickr.com/photos/35605239@N00/4035924977/" title="dashboard_server_summary by phunt, on Flickr"><img src="http://farm3.static.flickr.com/2630/4035924977_a18d7639f1.jpg" width="500" height="454" alt="dashboard_server_summary" /></a>

h3. ZNode tree

ACLs and child list not shown

<a href="http://www.flickr.com/photos/35605239@N00/4036673608/" title="dashboard_tree_znode by phunt, on Flickr"><img src="http://farm3.static.flickr.com/2495/4036673608_495c4594ef.jpg" width="500" height="457" alt="dashboard_tree_znode" /></a>
