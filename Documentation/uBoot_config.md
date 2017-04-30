# Configuring U-Boot on T1023RDB

Interrupt autoboot and enter U-Boot's command line interface by pressing any key at boot-up. Then enter the following commands (Note: tftpip should be the ip address of the tftp server):

Commands:
```sh
=> setenv ramdiskfile pason-image-wap-t1023rdb.ext2.gz.u-boot 
=> setenv fdtfile uImage-t1023rdb.dtb 
=> setenv krnlfile uImage-t1023rdb.bin 
=> setenv krnladdr $loadaddr 
=> setenv tftpkrnl tftpboot $krnladdr $krnlfile 
=> setenv tftpfdt tftpboot $fdtaddr $fdtfile 
=> setenv tftpramdisk tftpboot $ramdiskaddr $ramdiskfile 
=> setenv tftpip 172.19.2.194 
=> setenv bootnand "$bootcmd" 
=> setenv bootcmd dhcp\;setenv serverip $tftpip\;run tftpkrnl\;run tftpfdt\;run tftpramdisk\;bootm $krnladdr $ramdiskaddr $fdtaddr 
=> saveenv 
=> run bootcmd
```