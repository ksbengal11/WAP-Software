# Running batman-vis and alfred
Start alfred in master mode. Masters announce their staus via broadcast so slaves can find them. 

Open a terminal and enter:
``` sh
$ sudo alfred -i bat0 -m
```

Batman-vis combines server (daemon) and client functionality. Batadv-vis server must be started to let batadv-vis work. This server will read neighbor and client information from batman-adv every 10 seconds and set it in alfred via unix socket. (The alfred server needs to be running as well) 

Open a **second terminal** and enter:
``` sh
$ sudo batadv-vis -i bat0 -s
```

To display a graphviz-compatible output, open a **third terminal** and enter:
``` sh
$ sudo batadv-vis
```

The graphvis compatible output can be converted to an image as follows.
``` sh
$ sudo batadv-vis > mesh_network.dot
$ sudo dot -Tpng mesh.dot -o mesh.png
```