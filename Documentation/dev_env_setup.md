# Dev Env Setup

Commands for setting up the development environment

Official Documentation:
http://www.nxp.com/assets/documents/data/en/application-notes/AN5340.pdf

Commands:
```sh
$ sudo mount -o loop /home/<username>/Downloads/QorIQ-SDK-V2.0-20160527-yocto /mnt
$ cd /mnt/
$ ./install
$ cd ~
$ cd QorIQ-SDK-V2.0-20160527-yocto/sources/meta-freescale/scripts/ 
$ ./host-prepare.sh 
$ cd ~ 
$  cd QorIQ-SDK-V2.0-20160527-yocto/sources/ 
$ git clone https://bitbucket.org/naveedkawsar/wap-meta.git meta-pason 
$ cd ~ 
$ cd QorIQ-SDK-V2.0-20160527-yocto/  
$ MACHINE=t1023rdb source ./fsl-setup-env -b build_t1023rdb/ 
$ echo 'BBLAYERS += "/home/<username>/QorIQ-SDK-V2.0-20160527-yocto/sources/meta-pason" ' >> ~/QorIQ-SDK-V2.0-20160527-yocto/build_t1023rdb/conf/bblayers.conf 
$ bitbake pason-image-wap 
$ sudo apt-get install tftpd-hpa 
$ sudo rm –rf /srv/tftp 
$ sudo ln -s QorIQ-SDK-V2.0-20160527-yocto/build_t1023rdb/tmp/deploy/images/t1023rdb /srv/tftp
```
