import os
import pyglet

def apply(scene):
    # try to find soundfile
    path = os.path.join(os.getcwd(),scene["audio"])
    if os.path.exists(path):
        # play it
	play(path)
    else:
        print ("Soundfile not found at "+path)



def play(file):
    player = pyglet.media.Player()
    song = pyglet.media.load(file)
    player.queue(song)
    player.eos_loop = "loop"
    print("Started Player")
    try:
	player.play()
        pyglet.app.run()
    except KeyboardInterrupt:
        pass
    print("Player stopped")

