import os
import json
import logging
from atmosphuer import AtmosphuerBridge
from flask import Flask, render_template, request, jsonify
from flask_navigation import Navigation

app = Flask(__name__)
nav = Navigation(app)

bridge = AtmosphuerBridge()

@app.route('/')
def index():
    logging.debug("/index")
    return render_template('index.html', lights=bridge.get_lights(), scenes=bridge.get_scenes(), sounds=bridge.get_sounds())


@app.route('/togglelight',  methods=["POST"])
def togglelight():
    logging.debug("/togglelight")
    response = request.get_json()
    bridge.bridge.set_light(int(response['id']), 'on', response['on'], CONFIG['transition'])
    return jsonify(success=True)


@app.route('/applyscene', methods=["POST"])
def applyscene():
    logging.debug("/applyscene")
    for s in bridge.bridge.scenes:
        if s.name == request.get_json()['name']:
            bridge.bridge.activate_scene(0, s.scene_id)  # use group_id 0 to activate all lights of the scene
    return jsonify(success=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
