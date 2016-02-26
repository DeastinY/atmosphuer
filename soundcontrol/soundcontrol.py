import os
import logging
import subprocess

logger = logging.getLogger(__name__)

path = os.path.abspath(os.path.join(os.path.abspath(__file__), os.pardir, os.pardir, 'static', 'sounds'))

"""
Returns a list of all sounds from the static/sounds directory
"""


def getsounds():
    sounds = []
    for file in os.listdir(path):
        if file[-3:].casefold() == "mp3":
            sounds.append(file)
    logger.info("Loaded sounds " + str(sounds))
    return sorted(sounds)


"""
Downloads a video from youtube
"""


def youtubedl(url, name):
    command = "youtube-dl --extract-audio --audio-format mp3 --output " +os.path.join(path,name[0]+'.mp3')+" --force-ipv4 "+url[0]
    try:
        subprocess.call(command.split())
    except Exception as e:
        logger.exception(e)
