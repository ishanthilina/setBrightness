#!/usr/bin/env python

#setBrightness:: A script to set the display brightness automatically to
#the desired value at the startup.
#
#Author: Ishan Thilina Somasiri
#E-mail: ishan@ishans.info
#Version: 1
#Release date: 25th Sep 2011
#


import dbus
bus = dbus.SessionBus()

###################################################
#Change this value to change the startup brightness
value=0
###################################################

proxy = bus.get_object('org.gnome.PowerManager',
                       '/org/gnome/PowerManager/Backlight')

iface=dbus.Interface(proxy,dbus_interface='org.gnome.PowerManager.Backlight')

iface.SetBrightness(value)
