#!/usr/bin/python

from phue import Bridge
import logging

#set up a basic config for the logger
logging.basicConfig()

b = Bridge('192.168.0.10')
lamp = {}

# If the app is not registered and the button is not pressed, press the button and call connect() (this only needs to be run a single time)
b.connect()
print("bridge connected")

# Get the names to all the lamps
print("found lamps:")
for i in range (3):
    name = b.get_light(i+1,'name')
    lamp[name] = i

print("\t"+str(lamp))

# Get the bridge state (This returns the full dictionary that you can explore) (b.get_api())

# Prints if light 1 is on or not b.get_light(1, 'on')

# Set brightness of lamp 1 to max b.set_light(1, 'bri', 254)

# Set brightness of lamp 2 to 50% b.set_light(2, 'bri', 127)

# Turn lamp 2 on b.set_light(2,'on', True)

# You can also control multiple lamps by sending a list as lamp_id b.set_light( [1,2], 'on', True)

# Get the name of a lamp b.get_light(1, 'name')

# You can also use light names instead of the id b.get_light('Kitchen') b.set_light('Kitchen', 'bri', 254)

# Also works with lists b.set_light(['Bathroom', 'Garage'], 'on', False)

# The set_light method can also take a dictionary as the second argument to do more fancy stuff
# This will turn light 1 on with a transition time of 30 seconds
# command =  {'transitiontime' : 300, 'on' : True, 'bri' : 254}
# b.set_light(1, command)
