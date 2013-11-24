# Bluetooth-lookup
================

Look up Bluetooth devices using python. 


### You will need:
> 1. A Raspberry Pi computer, I tested with the 512 MB model, with internet connection.
> 2. An SD card loaded with the latest Raspbian .wheezy. software. [Download](http://www.raspberrypi.org/downloads)
> 3. A supported Bluetooth USB dongle. [Adapters](http://elinux.org/RPi_USB_Bluetooth_adapters)
> 4. Putty terminal client [Download](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html)

* sudo apt-get install bluez
* sudo apt-get install python-bluez

If you have not already, insert your bluetooth dongle into a USB port on the pi.
At the terminal you can use hcitool to check your device, e.g. type

hcitool dev
