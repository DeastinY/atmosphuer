import os
import json
import logging
from pathlib import Path
from phue import Bridge
from flask import Flask, render_template, request, jsonify
from flask_navigation import Navigation

logging.basicConfig(level=logging.INFO)
CONFIG = None
BASE_PATH = os.path.dirname(__file__)
CONFIG_FILE = Path(BASE_PATH, "settings.json")

class AtmosphuerBridge():
    def __init__(self, debug=False):
        self.check_config()
        self.bridge = Bridge(CONFIG['bridge_ip'])
        self.sound_path = Path(CONFIG["sound_dir"])
        self.sound_path.mkdir(exist_ok=True)
        print_settings_help()

    def check_config(self):
        global CONFIG
        if CONFIG_FILE.exists():
            CONFIG = json.loads(CONFIG_FILE.read_text())
        else:
            CONFIG = {
                "lights": [
                    "Decke Esszimmer",
                    "Spot Esszimmer",
                    "Fluter Esszimmer"
                ],
                "bridge_ip": "192.168.178.25",
                "owners": [
                    "49Kq0zuHbXWFSX0zyhayFP2Ok19cQapAvSoQwyBI",
                    "ZP7F5rqLi7PleAqpna8mVic0mLLYC6Ft3r6S5yXJ",
                    "MC96Eqy6UVKBIfUq6exDZBBf9orGbqzU39lvB1DU",
                    "4OL6W0jrLzLUubiK0u-xA779Up89-SevTCBgbPOd"
                ],
                "sound_dir": "/home/ric/projects/shadowrun/atmosphuer/static/sounds",
                "transition": 1000
            }
            CONFIG_FILE.write_text(json.dumps(CONFIG, indent=2))
            logging.warning("Create config file, please configure the program now !")
            import sys
            sys.exit()

    def get_lights(self):
        """Returns a list of all lights from config with (name, id, on)"""
        return sorted(
            [(l.name, self.bridge.get_light_id_by_name(l.name), l.on) for l in self.bridge.lights if l.name in CONFIG['lights']]
            , key=lambda l: l[0])


    def get_scenes(self):
        scenes = []
        for scene in self.bridge.scenes:
            if scene.owner in CONFIG['owners']:
                if any([self.bridge.get_light(l, 'name') not in CONFIG['lights'] for l in scene.lights]):
                    continue
                else:
                    scenes.append(scene)
        return sorted(scenes, key=lambda s: s.name)

    def get_sounds(self):
        sounds = []
        for file in self.sound_path.iterdir():
            sounds.append(file.name)
        return sounds

    def print_settings_help(self):
        logging.info("Use the following to select the right lights and owners:")
        for l in self.bridge.lights:
            logging.info(f"\t{l.name}")
        owners_logged = []
        for s in self.bridge.scenes:
            if s.owner not in owners_logged:
                logging.info(f"\t{s.name}, {s.owner}")
                owners_logged.append(s.owner)





