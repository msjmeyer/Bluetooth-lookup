Bluetooth-lookup
================

Look up Bluetooth devices using python. 


You will need:
A Raspberry Pi computer, I tested with the 512 MB model, with internet connection.
An SD card loaded with the latest Raspbian .wheezy. software. See http://www.raspberrypi.org/downloads for how to get that setup.
A supported bluetooth USB dongle. See http://elinux.org/RPi_VerifiedPeripherals#USB_Bluetooth_adapters
Some way to access a terminal on the Pi. I used ssh, or just use the normal desktop and open Terminal.


sudo apt-get install bluez
sudo apt-get install python-bluez

If you have not already, insert your bluetooth dongle into a USB port on the pi.
At the terminal you can use hcitool to check your device, e.g. type

hcitool dev

