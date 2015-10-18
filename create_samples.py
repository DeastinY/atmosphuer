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
settings = util.load_or_sample("settings", jsonhandler.load_settings, jsonhandler.write_sample_settings)

# (later from JSON)
b = phue.Bridge(settings["bridge_ip"])

# If the app is not registered and the button is not pressed, press the button and call connect() (this only needs to be run a single time)
b.connect()
print("Bridge connected")

# Get all the lights
lights = b.get_light_objects('name')

# Set up relevant SR lights (later from JSON)
sr = [lights[settings["shadowrun_lights"]]]

# Ask user for input until he closes the program
while True:
    print ("Enter end to exit")
    i = input("Enter Name for Scene:\t")
    if i == "end":
        sys.exit()
    # Take value from first light
    h = sr[0].hue
    s = sr[0].saturation
    b = sr[0].brightness
    jsonhandler.appendCreatedSample(h,s,b,i)
