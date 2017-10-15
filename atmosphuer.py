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

BRIDGE = Bridge(CONFIG['bridge_ip'])
SOUND_PATH = Path(CONFIG["sound_dir"])
SOUND_PATH.mkdir(exist_ok=True)


def print_settings_help():
    logging.info("Use the following to select the right lights and owners:")
    for l in BRIDGE.lights:
        logging.info(f"\t{l.name}")
    owners_logged = []
    for s in BRIDGE.scenes:
        if s.owner not in owners_logged:
            logging.info(f"\t{s.name}, {s.owner}")
            owners_logged.append(s.owner)

print_settings_help()


def get_lights():
    """Returns a list of all lights from config with (name, id, on)"""
    return sorted(
        [(l.name, BRIDGE.get_light_id_by_name(l.name), l.on) for l in BRIDGE.lights if l.name in CONFIG['lights']]
        , key=lambda l: l[0])


def get_scenes():
    scenes = []
    for scene in BRIDGE.scenes:
        if scene.owner in CONFIG['owners']:
            if any([BRIDGE.get_light(l, 'name') not in CONFIG['lights'] for l in scene.lights]):
                continue
            else:
                scenes.append(scene)
    return sorted(scenes, key=lambda s: s.name)


def get_sounds():
    sounds = []
    for file in SOUND_PATH.iterdir():
        sounds.append(file.name)
    return sounds

app = Flask(__name__)
nav = Navigation(app)


@app.route('/')
def index():
    logging.debug("/index")
    return render_template('index.html', lights=get_lights(), scenes=get_scenes(), sounds=get_sounds())


@app.route('/togglelight',  methods=["POST"])
def togglelight():
    logging.debug("/togglelight")
    response = request.get_json()
    BRIDGE.set_light(int(response['id']), 'on', response['on'], CONFIG['transition'])
    return jsonify(success=True)


@app.route('/applyscene', methods=["POST"])
def applyscene():
    logging.debug("/applyscene")
    for s in BRIDGE.scenes:
        if s.name == request.get_json()['name']:
            BRIDGE.activate_scene(0, s.scene_id)  # use group_id 0 to activate all lights of the scene
    return jsonify(success=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
