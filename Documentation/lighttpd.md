# Installing and Configuring Lighttpd
Go to home directory
``` sh
$ cd ~/
```
Install Lighttpd
``` sh
$ sudo apt-get install lighttpd
```
Install Flask python framework
``` sh
$ sudo apt-get install python-flup
```
Pull this repository and navigate to "Lighttpd" folder
``` sh
$ git pull ...
```
Copy the lighttpd configuration file, "lighttpd.conf" to "/etc/lighttpd/"
``` sh
$ sudo cp ~/wap-software/CapstoneFair/Lighttpd/lighttpd.conf /etc/lighttpd/
```
Copy the "www/" directory from the lighttpd folder to "/var/"
``` sh
$ sudo cp -R ~/wap-software/CapstoneFair/Lighttpd/www /var/
```
Start the lighttpd service
``` sh
$ sudo service lighttpd start
```
Open a web - browser and navigate to "http://localhost/myapp/test.py"

### Commands

Useful commands for debugging

Start the lighttpd service
``` sh
$ sudo service lighttpd stop
```
Restart the lighttpd service
``` sh
$ sudo service lighttpd restart
```
Check lighttpd status
``` sh
$ sudo service lighttpd status
```
Location of lighttpd error log
``` sh
$ cat /var/log/lighttpd/error.log
```