from collections import namedtuple
import operator
import logging
import os
import json

logger = logging.getLogger(__name__)
scenespath = os.path.abspath(os.path.join(os.path.abspath(__file__), os.pardir, os.pardir, 'scenes.json'))
SceneTuple = namedtuple('Scene', 'name hue brightness saturation hits')


class Scene:
    def __init__(self, saturation = None, hue = None, brightness = None, name = "unnamed", hits = None):
        self.saturation = saturation or 0
        self.hue = hue or 0
        self.brightness = brightness or 0
        self.name = name or "unnamed"
        self.hits = hits or 0

    def __str__(self):
        return str(self.namedtupledict)

    def __repr__(self):
        return str(self.namedtupledict)

    @property
    def namedtuple(self):
        return SceneTuple(self.name,self.hue,self.brightness,self.saturation,self.hits)

    @property
    def namedtupledict(self):
        return self.namedtuple._asdict()

    @staticmethod
    def saveall(scenes):
        logger.info("Saving Scenes")
        try:
            with open(scenespath, 'w') as outfile:
                outfile.write(json.dumps([a.namedtupledict for a in scenes], sort_keys=True, indent=4, separators=(',', ': ')))
        except Exception as e:
            logger.exception(e)

    @staticmethod
    def fromJSON(jscene):
        logger.info("Loading Scenes")
        return Scene(name=jscene['name'], hue=jscene['hue'], brightness=jscene['brightness'],saturation=jscene['saturation'],hits=jscene['hits'])

    @staticmethod
    def loadall():
        try:
            with open(scenespath, 'r') as infile:
                scenes = json.loads(infile.read())
                # Convert to Scenes
                scenes = [Scene.fromJSON(s) for s in scenes]
                # Sort by hits and return
                return Scene.sort(scenes)
        except Exception as e:
            logger.exception(e)

    @staticmethod
    def sort(scenes):
        scenes.sort(key=lambda s: (s.name)) #add -s.hits before s.name for sorting with hits
        return scenes