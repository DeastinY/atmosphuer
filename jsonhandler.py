import json
import os

# Fix Python 2.x.
try: input = raw_input
except NameError: pass

def appendCreatedSample(hue, saturation, brightness, name):
    f = open ("createdSamples.json", "a")
    json_scene = {
        "name": name,
        "brightness": brightness,
        "hue": hue,
        "saturation": saturation,
        "audio": name+".mp3",
    }
    f.write(json.dumps(json_scene))
    f.write(",\n")
    f.close()

def write_sample(content, filename):
    f = open (filename, "w")
    f.write(json.dumps(content))
    f.close()

def write_sample_settings(SaveAsOriginal):
    #{"bridge_ip": "192.168.0.10", "shadowrun_lights": "Arbeitszimmer"}
    json_settings = {
        "bridge_ip": "192.168.0.10",
        "shadowrun_lights": "Arbeitszimmer",
    }


    fsettings = "settings_sample.json"
    if SaveAsOriginal:
        fsettings = "settings.json"

    write_sample(json_settings, fsettings)

    print("Sample Setting written")

def write_sample_scenes(SaveAsOriginal):
    #{"name": "rain", "brightness": "254", "hue": "15000", "saturation": "120", "audio": "rain.mp3" }
    json_scenes = [{
        "name": "rain",
        "brightness": "254",
        "hue": "15000",
        "saturation": "120",
        "audio": "rain.mp3",
    }]

    fscenes = "scenes_sample.json"
    if SaveAsOriginal:
        fscenes = "scenes.json"

    write_sample(json_scenes,fscenes)

    print ("Sample Scenes written")


def load_settings():
    settings = os.path.join(os.getcwd(),"settings.json")
    return load(settings)

def load_scenes():
    scenes = os.path.join(os.getcwd(),"scenes.json")
    return load(scenes)

def load(filename):
    if os.path.exists(filename):
        print("Loading "+filename)
        file = open(filename,"r")
        content = file.read()
        file.close()
        return json.loads(content)
    else:
        print ("Could not find file "+filename)
        print ("Exiting")
