#!/usr/bin/python
"""
Author: 	Karan Bengali, Haider Ali, John Li
Version: 	1.0
Since: 		March 25, 2017
"""

# import objects from the Flask model
from flask import Flask, render_template, request, json
import subprocess

app = Flask(__name__)

# Prints stack trace on the webserver if there is an error in our code
app.config.update(PROPAGATE_EXCEPTIONS=True)

class Wap():
	def __init__(self):
		#Initialize the rssi list
		self.rssi = {"dev_addr1": 0, "dev_addr2": 0, "dev_addr3": 0,
					"dev_addr4": 0}

wapDevice = Wap()

@app.route('/', methods=['GET', 'POST'])
def returnAll():
	"""
	Return a list containing rssi values of each access point. HTTP post
	requests are read and parsed to update the rssi list.

	Renders HTML template in 'template.html' to display on webserver

	@return: HTML template
	@return: list containing rssi values of access points
	"""
	if(request.method=='POST'):
		for key in request.json:
			wapDevice.rssi[key] = request.json[key]
		return render_template('template.html', result=wapDevice.rssi)

	return render_template('template.html', result=wapDevice.rssi)

@app.route('/cakes')
def cakes():
	"""
	Used for debugging purposes only. Displays Yummy Cakes on the webserver
	"""
	return "Yummy Cakes!"

if __name__ == '__main__':
	"""
	Default entry point.
	Uncomment line 57 and comment out lines 55 and 56 to run a flask webserver.
	"""
	from flup.server.fcgi import WSGIServer
	WSGIServer(app).run()
	#app.run(debug=True, port=5000, host=0.0.0.0)
