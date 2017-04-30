# Wap-Software
Webserver implementation

---
**Contributers:**  
- Karan Bengali  
- Naveed Kawsar  
- Haider Ali  
- John Li  

**Version:** 1.0  
**Since:** April 12, 2017

---
**Documentation:**  
- Development environment setup  
- UBoot configuration  
- USB Booting commands  
- Configuring Lighttpd webserver  
- Installing batman-adv  
- Installing batctl  
- Running Batman-vis  
---
**Folder:** *Batman-adv*  
Contains a script to automatically configure batman-adv interface on the test laptop.  
  
To run the script enter:  

```
#!command line

sudo ./batmesh.sh
```
---
**Folder:** *CapstoneFair/Lighttpd*  
Contains lighttpd configuration file, front-end and back-end programs for implementing a lighttpd webserver.  
  
To run the webserver, configure lighttpd as described in the documentation.  

```
#!command line

sudo service lighttpd start
sudo service lighttpd status
```  

If the service start without errors, visit *"http://localhost/myapp/test.py/"*  
    
---
Network map will be automatically updated after entering the following commands:

```
#!command line
sudo ./map_generator.sh
```  
**Note:** The Alfred and Batman-vis server must be running before the network map can be displayed.  
  
---
The RSSI chart will display values after running the following program:
```
#!command line
sudo python iwlist.py
```  
---
The Access Point Configuration page can be visited here:*"http://localhost/myapp/config_page.py/"*