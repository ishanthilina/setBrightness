#!/usr/bin/python
import argparse
import dbus
import datetime

# Level settings:
day_level=75
night_level=20

bus = dbus.SessionBus()

proxy = bus.get_object('org.gnome.SettingsDaemon',
                       '/org/gnome/SettingsDaemon/Power')
#print proxy

iface=dbus.Interface(proxy,dbus_interface='org.gnome.SettingsDaemon.Power.Screen')

# Description
parser = argparse.ArgumentParser(description='Sets the Monitor Brightness')

# Set int argument:
parser.add_argument("level", nargs="?", type=int, help='Integer from 1 to 100')
# nargs="?" wont make error if missing argument

args = parser.parse_args()

#print 'Bright: ', args.level

if not args.level:
  
  # Setting brightness based on time:
  print "Setting brightness based on Time"
  
  now = datetime.datetime.now()
  #print "Current hour: %d" % now.hour

  if now.hour > 7 and now.hour < 20:
    level = day_level
    #print "Brigthness Changed"
  else:
    level = night_level
    
else:
  level = args.level
  
print "Setting brightness to: ", level

# Set brightness:
try:
  iface.SetPercentage(level)
except:
  print "Wrong brightness input: \nplease enter int from 1 to 100"
