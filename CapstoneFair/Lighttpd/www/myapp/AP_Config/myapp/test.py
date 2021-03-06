#!/usr/bin/python

# import objects from the Flask model
from flask import Flask, jsonify, render_template, json, request
import subprocess, serial, time

interface = "wlan0"
# url of our webserver
#url = "http://172.19.2.5/myapp/test.py/"

app = Flask(__name__)

# Prints stack trace on the webserver if there is an error in our code
app.config.update(PROPAGATE_EXCEPTIONS=True)

#class wap():
#	def __init__(self):
#		self.dev_params = {"Name": "pason-ap", "Address": 0, "Encryption": 0, "Signal": 0, "Channel":0}

#dev1 = wap()
#dev2 = wap()
#dev3 = wap()
#dev4 = wap()

# Dictionary containing all access points
dev_list = {'00:0E:8E:6F:DD:D2': 0, '00:0E:8E:6F:DD:D8': 0, '00:0E:8E:6F:DD:D6': 0, '00:0E:8E:6F:DD:DA': 0}

# For debugging purposes only.
@app.route('/', methods=['GET', 'POST'])
def returnAll():
	if(request.method == 'POST'):
		for key in request.json:
			dev_list[key] = request.json[key]
	return render_template('template.html',result=dev_list)

@app.route('/_AP_config')
def ap_config():
	return render_template('config_page.html')


@app.route('/_config')
def config():
		ser = serial.Serial(
			port='/dev/ttyS0',
			baudrate=115200,
			timeout=1
		)
		ser.close()
		ser.open()

		new_ssid = request.args.get('new_ssid', "Nothing was entered", type=str)
		new_chan = request.args.get('new_chan', "Nothing was entered", type=str)

		changed_ss = False
		changed_chan = False

		if len(str(new_ssid)) == 0:
			time.sleep(0)
		else:
			'''cmd = "sed -i 's/^\(ssid\s*=\s*\).*$/\ssid="+str(new_ssid)+"/' /etc/hostapd.conf"
			ser.write(cmd.encode('ascii')+ '\r\n')
			time.sleep(1)'''
			changed_ss = True

		if len(str(new_chan)) == 0:
			time.sleep(0)
		else:
			'''cmd = "sed -i 's/^\(channel\s*=\s*\).*$/channel="+str(new_chan)+"/' /etc/hostapd.conf"
			ser.write(cmd.encode('ascii')+ '\r\n')
			time.sleep(1)'''
			changed_chan = True

		if (changed_ss or changed_chan) == True:
			'''cmd = "/etc/init.d/hostapd restart"
			ser.write(cmd.encode('ascii')+ '\r\n')
			ser.close()
			time.sleep(1)'''
		else:
			time.sleep(0)

		new_meshid = request.args.get('new_meshid', "Nothing was entered", type=str)
		if len(str(new_meshid)) == 0:
			time.sleep(0)
		'''else:
				cmd = "iwconfig wlan1 essid "+str(new_meshid)
				ser.write(cmd.encode('ascii')+ '\r\n')
				time.sleep(1)'''

		cmd = "source /etc/hostapd.conf && echo $ssid && echo $channel"
		ser.write(cmd.encode('ascii') + '\r\n')
		incoming = ""
		time.sleep(1)
		while ser.inWaiting() > 0:
			incoming += ser.read(1);
		current_value = incoming.split("\r\n")
		cmd = "iwconfig wlan1"
		ser.write(cmd.encode('ascii')+'\r\n')
		time.sleep(0.5)
		incoming = ""
		while ser.inWaiting() > 0:
			incoming += ser.read(1)
		ser.close()
		get_essid = incoming.split( )
		get_essid1 = get_essid[5].split(':')
		get_essid = get_essid1[1].split('"')

		return jsonify(current_meshid=get_essid[1],current_ssid=current_value[1],current_channel=current_value[2].strip('\n'))

@app.route('/_first_run')
def populate():
		ser = serial.Serial(
			port='/dev/ttyS0',
			baudrate=115200,
			timeout=1
		)

		ser.close()
		ser.open()
		cmd = "source /etc/hostapd.conf && echo $ssid && echo $channel"
		ser.write(cmd.encode('ascii') + '\r\n')
		incoming = ""
		time.sleep(1)
		while ser.inWaiting() > 0:
			incoming += ser.read(1);
		current_value = incoming.split("\r\n")
		cmd = "iwconfig wlan1"
		ser.write(cmd.encode('ascii')+'\r\n')
		time.sleep(0.5)
		incoming = ""
		while ser.inWaiting() > 0:
			incoming += ser.read(1)
		ser.close()
		get_essid = incoming.split( )
		get_essid1 = get_essid[5].split(':')
		get_essid = get_essid1[1].split('"')
		return jsonify(current_meshid=get_essid[1],current_ssid=current_value[1],current_channel=current_value[2].strip('\n'))

#Function used for debugging only
@app.route('/cakes')
def cakes():
	return jsonify(wap['dev1'])

if __name__ == '__main__':
	from flup.server.fcgi import WSGIServer
	WSGIServer(app).run()
	#app.run(debug=True)
