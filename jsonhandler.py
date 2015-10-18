import json
import os

def write_sample_json_file(SaveAsOriginal):
    print("Writing Samples")
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
    fscenes = "scenes_sample.json"
    fsettings = "settings_sample.json"
    if SaveAsOriginal:
        fscenes = "scenes.json"
        fsettings = "settings.json"

    f = open(fscenes,"w")
    f.write(json.dumps(json_scenes))
    f.close()

    f = open(fsettings,"w")
    f.write(json.dumps(json_settings))
    f.close()

    print("Files written")

def load_settings():
    settings = os.path.join(os.getcwd(),"settings.json")
    return load(settings)

def load_scenes():
    settings = os.path.join(os.getcwd(),"scenes.json")
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
