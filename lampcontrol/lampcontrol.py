from collections import namedtuple
import os
import phue
import json
import logging
from lampcontrol.Scene import Scene

logger = logging.getLogger(__name__)

Light = namedtuple('Light', 'name on')

try:
    # setup lamps on first startup
    bridge = phue.Bridge("192.168.0.10")  # TODO: Bad hardcoded string

    logger.info(bridge.connect())
except phue.PhueRequestTimeout:
    logger.warning("Could not connect to Hue. Connection timed out.")
except Exception as e:
    logger.exception(e)

"""
Returns a list of named tuples containing name and state
"""


def getlights():
    try:
        lights = bridge.lights
        sortedlights = sorted([Light(str(l.name), l.on) for l in lights])
        return sortedlights
    except:
        logger.warning("Could not get lights from Hue")


"""
Sets a lamp to a defined state
"""


def setlight(name, on):
    try:
        bridge.set_light(name,'on',on)
    except Exception as e:
        logger.exception(e)


"""
Sets a scene
"""


def setscene(scene):
    try:
        scene.hits += 1
        for l in getlights():
            if l.on:
                command = {'bri' : int(scene.brightness), 'sat' : int(scene.saturation), 'hue' : int(scene.hue)}
                bridge.set_light(l.name,command)
    except Exception as e:
        logger.exception(e)
