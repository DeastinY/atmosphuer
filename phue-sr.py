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
scenes = util.load_or_sample("scenes",jsonhandler.load_scenes, jsonhandler.write_sample_scenes)

# Ask user for input until he closes the program
i = ""
while i != "end":
    util.print_options(scenes)
    i = input("Enter command:")

# Deactivate lamp
for light in sr:
    light.on = False
