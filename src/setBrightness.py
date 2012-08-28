#!/usr/bin/python
import argparse
import dbus
import datetime
import ConfigParser
import os

##Load configuration data
config = ConfigParser.RawConfigParser()
config.read(os.path.expanduser("~") + "/.setBrightness/" + "config.cfg")

##get the dbus interfaces
bus = dbus.SessionBus()

proxy = bus.get_object('org.gnome.SettingsDaemon',
                       '/org/gnome/SettingsDaemon/Power')

iface = dbus.\
  Interface(proxy, dbus_interface='org.gnome.SettingsDaemon.Power.Screen')

##code required for argument parsing
# Description
parser = argparse.ArgumentParser(description='Sets the Monitor Brightness')

# Set int argument:
parser.add_argument("level", nargs="?", type=int, help='Integer from 1 to 100')
# nargs="?" wont make error if missing argument

args = parser.parse_args()

#if no paramenters are present
if not args.level and args.level != 0:

    #load settings from config file
    if config.getboolean('dynamic', 'enabled'):
        # Setting brightness based on time:
        print "Setting brightness based on Time"

        now = datetime.datetime.now()

        if now.hour > 7 and now.hour < 20:
            level = config.getint("values", "day")
        else:
            level = config.getint("values", "night")

    #if dynamic brightness changes are not enabled
    else:
        level = config.getint("values", "default")
else:
        level = args.level

print "Setting brightness to: ", level

# Set brightness:
try:
    iface.SetPercentage(level)
except:
    print "Wrong brightness input: \nplease enter int from 1 to 100"
