from pygame import mixer

file = '<music_name.mp3>'
    # file name with path

mixer.init()
mixer.music.load(file)
mixer.music.play()