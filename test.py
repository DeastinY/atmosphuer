#!/usr/bin/python

from phue import Bridge
import logging
import json



# The set_light method can also take a dictionary as the second argument to do more fancy stuff
# This will turn light 1 on with a transition time of 30 seconds
# command =  {'transitiontime' : 300, 'on' : True, 'bri' : 254}
# b.set_light(1, command)
