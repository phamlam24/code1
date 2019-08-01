import pyglet
window = pyglet.window.Window()
music = pyglet.resource.media('file_example_MP3_700KB.mp3')
music.play()
pyglet.app.run()