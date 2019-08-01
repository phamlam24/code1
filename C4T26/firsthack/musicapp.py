import pyglet
# from pyglet.media import Source, Player, load

# player = Player()
# source = load("music.wav")
# player.queue(source)
# player.play()

music = pyglet.resource.media('music.wav')
music.play()



pyglet.app.run()