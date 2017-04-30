#!/bin/sh

#If joining mesh using physical interface
#sudo batctl if del eth0
#sudo ifconfig bat0 down
#sudo ifconfig eth0 down
#sudo ifconfig eth0 mtu 1532
#sudo batctl if add eth0
#sudo ifconfig eth0 up
#sudo ifconfig bat0 up
#sudo ifconfig bat0 192.168.0.8

#If joining mesh using wireless interface
sudo batctl if del wlan0
sudo ifconfig bat0 down
sudo ifconfig wlan0 down
sudo ifconfig wlan0 mtu 1532
sudo iw wlan0 set type ibss
sudo ip link set wlan0 up
sudo iw wlan0 ibss join pason-mesh 2462
sudo batctl if add wlan0
sudo ip link set bat0 up
sudo ifconfig wlan0 192.168.0.8

# Change the hop penalty to 255
echo 255 | sudo tee --append /sys/class/net/bat0/mesh/hop_penalty

