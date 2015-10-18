import phue
import jsonhandler
import util
import logging
import sys

#
# For config files :
# Brightness is set from 0 to 254
# Hue has the range 0-65535 (182 degrees)
# Saturation is set from 0 to 254
#


# Fix Python 2.x.
try: input = raw_input
except NameError: pass

# set up a basic config for the logger
logging.basicConfig()

# load settings
settings = util.load_or_sample("settings", None, jsonhandler.load_settings, jsonhandler.write_sample_settings)

# (later from JSON)
b = phue.Bridge(settings["bridge_ip"])

# If the app is not registered and the button is not pressed, press the button and call connect() (this only needs to be run a single time)
b.connect()
print("Bridge connected")

# Get all the lights
lights = b.get_light_objects('name')

# Set up relevant SR lights (later from JSON)
sr = [lights[settings["shadowrun_lights"]]]

# Activate lamp
for light in sr:
    light.on = True

# Load Scenes
scenes = util.load_or_sample("scenes", settings["scenes_file"],jsonhandler.load_scenes, jsonhandler.write_sample_scenes)

# Ask user for input until he closes the program
i = ""
while i != "end":
    util.print_options(scenes)
    i = input("Enter command:\t")
    # activate chosen setting
    try:
        ii = int(i)
        if ii > len(scenes)-1 or ii < 0:
            print ("invalid input")
        else:
            scene = scenes[ii]
            print ("Setting "+scene['name'])
            for light in sr:
                light.effect = "None"
                light.on = True
                light.brightness = int(scene['brightness'])
                light.saturation = int(scene['saturation'])
                light.hue = int(scene['hue'])
    except ValueError:
        pass

    # easteregg
    if i == "olf":
        util.easteregg(sr)


# Deactivate lamp
for light in sr:
    light.on = False
