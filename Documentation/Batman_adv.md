# Installing batman-adv 
Download the tar file
``` sh
$ sudo wget https://downloads.open-mesh.org/batman/releases/batman-adv-2016.5/batman-adv-2016.5.tar.gz  
```
Unzip the folder
``` sh
$ tar xvzf batman-adv-2016.5.tar.gz
```
In the MAKEFILE, change the line "export CONFIG_BATMAN_ADV_DEBUG=n" to "export CONFIG_BATMAN_ADV_DEBUG=y"

Make 
``` sh
$ sudo make
```
Install 
``` sh
$ sudo make install
```