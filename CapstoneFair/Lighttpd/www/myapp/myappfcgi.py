#!/usr/bin/python
from myapp import app

if __name__ == '__main__':
	from flup.server.fcgi import WSGIServer
	WSGIServer(app, bindAddress='/tmp/myapp-fcgi.sock').run()
