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
