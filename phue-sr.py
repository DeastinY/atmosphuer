import logging
import atexit
from flask import Flask, render_template, request, jsonify, redirect
from flask.ext.navigation import Navigation
from lampcontrol import lampcontrol
from soundcontrol import soundcontrol

class PhueSR:
    def __init__(self):
        self.lights = lampcontrol.getlights()
        self.scenes = lampcontrol.Scene.loadall()
        self.sounds = soundcontrol.getsounds()

    """
    Takes a scene name as input and returns the matching scene
    """
    def getscene(self, jscene):
        name = jscene['name']
        try:
            return next((s for s in self.scenes if s.name == name))
        except StopIteration:
            logging.warning("Internal scene not found !")

    """
    Reloads the lights
    """
    def reloadlights(self):
        self.lights = lampcontrol.getlights()

phuesr = PhueSR()


app = Flask(__name__)
nav = Navigation(app)
atexit.register(lampcontrol.Scene.saveall, phuesr.scenes)
logging.basicConfig(level=logging.DEBUG)


@app.route('/')
def index():
    # Refresh lights
    phuesr.reloadlights()
    # Resort Scenes
    phuesr.scenes = lampcontrol.Scene.sort(phuesr.scenes)
    return render_template('index.html', lights=phuesr.lights, scenes=phuesr.scenes, sounds=phuesr.sounds)

@app.route('/youtubedl', methods=["POST"])
def youtubedl():
    soundcontrol.youtubedl(**request.form)
    phuesr.sounds = soundcontrol.getsounds()
    return redirect('/')

@app.route('/togglelight',  methods=["POST"])
def togglelamp():
    lampcontrol.setlight(**request.get_json())
    return jsonify(success=True)


@app.route('/applyscene', methods=["POST"])
def applyscene():
    lampcontrol.setscene(phuesr.getscene(request.get_json()))
    return jsonify(success=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
