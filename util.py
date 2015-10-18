import time
import random

# Fix Python 2.x.
try: input = raw_input
except NameError: pass

def print_options(scenes):
    print("Here are the available options:")
    print("end\tEnd Programm")
    for i in range(len(scenes)):
        print(str(i)+"\t"+scenes[i]["name"])


def load_or_sample(name,file,loadFunc,writeFunc):
    loaded = loadFunc(file)
    if loaded == None:
        result = input("No "+name+" file has been found, do you want to create a sample ? [y/n] \n")
        if result == "y":
            writeFunc(True)
        loaded = loadFunc(file)
        if loaded == None:
            sys.exit()
    return loaded

def easteregg(sr):
    for light in sr:
        light.on = True
        light.brightness = 254
        light.saturation = 254
    # 1 Minute
    for i in range (210):
        for light in sr:
            # Adjust to 210 bpm of song
            time.sleep(.285)
            light.hue = random.randint(0,65535)
