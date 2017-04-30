# Installing batctl
Instal Batctl 
``` sh
$ sudo wget https://downloads.open-mesh.org/batman/releases/batman-adv-2016.5/batctl-2016.5.tar.gz   
```
Unzip the folder
``` sh
$ tar xvzf batctl-2016.5.tar.gz
```
Make 
``` sh
$ sudo make
```
Install 
``` sh
$ sudo make install
```
Install bridge-utils packet
``` sh
$ sudo apt-get install batctl bridge-utils
```
**Important:** You need root access to run batctl commands
# Useful commands
Displaying originator table
``` sh
$ sudo batctl o
```
Displaying neighbor table
``` sh
$ sudo batctl n
```
**Note** This will not work if you haven't enabled debugfs when installing batman-adv. See batman-adv documentation for more information

Sending a batctl ping
``` sh
$ sudo batctl ping <ip/mac_address>
```