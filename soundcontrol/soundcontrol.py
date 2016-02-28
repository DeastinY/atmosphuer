import os
import logging
import subprocess
import youtube_dl

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
    logger.info("Downloading"+url[0])
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors':[{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': True,
        'restrictfilenames' : True,
        'outtmpl': os.path.join(path,name[0]) + '.(ext)s'
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url[0]])
        except:
            logger.exception(e)
