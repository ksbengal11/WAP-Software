#!/bin/bash

echo
echo $0
echo Author: Karan Bengali
echo Version: 1.0
echo Since: March, 2017
echo
echo Procedure:
echo Store batadv-vis output in mesh.dot
echo mesh.dot is then converted to a png file mesh.png using graphviz
echo mesh.png is moved to /var/www/myapp/templates/
echo Interval = 5s
echo

while true
do
	sudo batadv-vis | grep -v "TT" > mesh.dot
	sudo dot -Tpng mesh.dot -o mesh.png
	sudo mv mesh.png /var/www/myapp/templates/
	echo Mesh updated ...
	sleep 5
done
