import pyglet

music = pyglet.resource.media('sample.mp3')
music.play()
pyglet.app.run()