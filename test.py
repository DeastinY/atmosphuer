#!/usr/bin/python

from phue import Bridge
import logging
import json

def print_options():
    print("")
    print("")
    print("")
    print("Here are the available options:")
    print("end\tEnd Programm")
    print("cs\tCreate Settings")
    pass

def write_sample_json_file():
    print("writing json samples")
    #{"name": "rain", "brightness": "254", "hue": "15000", "saturation": "120", "audio": "rain.mp3" }
    json_scenes = {
        "name": "rain",
        "brightness": "254",
        "hue": "15000",
        "saturation": "120",
        "audio": "rain.mp3",
    }

    #{"bridge_ip": "192.168.0.10", "shadowrun_lights": "Arbeitszimmer"}
    json_settings = {
        "bridge_ip": "192.168.0.10",
        "shadowrun_lights": "Arbeitszimmer",
    }

    #write to file
    f = open("scenes.json","w")
    f.write(json.dumps(json_scenes))
    f.close()

    f = open("settings.json","w")
    f.write(json.dumps(json_settings))
    f.close()

    print("files written")

#set up a basic config for the logger
logging.basicConfig()

# (later from JSON)
b = Bridge('192.168.0.10')

# If the app is not registered and the button is not pressed, press the button and call connect() (this only needs to be run a single time)
b.connect()
print("bridge connected")

# Get all the lights
print("found lamps:")
lights = b.get_light_objects('name')
for light in lights:
    print ("\t"+light)

    # Set up relevant SR lights (later from JSON)
    sr = [lights["Arbeitszimmer"]]#,lights[]"Esszimmer"]]

    # Activate lamp
    for light in sr:
        light.on = True
        light.brightness = 254


# Ask user for input until he closes the program
input = ""
while input != "end":
    print_options()
    input = raw_input("Enter command:")
    if input == "cs":
        write_sample_json_file()

# Deactivate lamp
for light in sr:
    light.on = False

# The set_light method can also take a dictionary as the second argument to do more fancy stuff
# This will turn light 1 on with a transition time of 30 seconds
# command =  {'transitiontime' : 300, 'on' : True, 'bri' : 254}
# b.set_light(1, command)
