def apply(scene,sr):
    for light in sr:
        light.on = True
        light.brightness = int(scene['brightness'])
        light.saturation = int(scene['saturation'])
        light.hue = int(scene['hue'])
