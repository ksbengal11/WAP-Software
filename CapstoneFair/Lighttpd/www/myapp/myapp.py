"""
This program is used for debugging Flask
"""

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello(environ, start_response):
	start_response('200 OK', [('Content-Type', 'text/plain')])
	return ['Hello World from Flask!!']

#if __name__ == '__main__':
#	app.run(host='0.0.0.0', port=5000)
