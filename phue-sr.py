import phue
import jsonhandler
import util
import logging
import sys

# Fix Python 2.x.
try: input = raw_input
except NameError: pass

# set up a basic config for the logger
logging.basicConfig()

# load settings

settings = util.load_or_sample("settings", jsonhandler.load_settings, jsonhandler.write_sample_settings)
#settings = jsonhandler.load_settings()
#if settings == None:
#if "y" == input("No settings file has been found, do you want to create a sample ? [y/n]\n"):
    #,jsonhandler.write_sample_settings(True)
#settings = jsonhandler.load_settings()
#if settings == None:
#    sys.exit()

# (later from JSON)
b = phue.Bridge(settings["bridge_ip"])

# If the app is not registered and the button is not pressed, press the button and call connect() (this only needs to be run a single time)
b.connect()
print("Bridge connected")

# Get all the lights
print("Found lamps:")
lights = b.get_light_objects('name')
for light in lights:
    print ("\t"+light)

# Set up relevant SR lights (later from JSON)
sr = [lights[settings["shadowrun_lights"]]]

# Activate lamp
for light in sr:
    light.on = True
    light.brightness = 254

# Load Scenes
scenes = jsonhandler.load_scenes()
if scenes == None:
    if "y" == input("No scenes file has been found, do you want to create a sample ? [y/n]\n"):
        jsonhandler.write_sample_scenes(True)
    scenes = jsonhandler.load_scenes()
    if scenes == None:
        sys.exit()



# Ask user for input until he closes the program
i = ""
while i != "end":
    util.print_options()
    i = input("Enter command:")

# Deactivate lamp
for light in sr:
    light.on = False
