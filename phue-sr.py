import phue
import jsonhandler
import utilities
import logging

#set up a basic config for the logger
logging.basicConfig()

# (later from JSON)
b = phue.Bridge('192.168.0.10')

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
    utilities.print_options()
    input = raw_input("Enter command:")
    if input == "cs":
        jsonhandler.write_sample_json_file()

# Deactivate lamp
for light in sr:
    light.on = False