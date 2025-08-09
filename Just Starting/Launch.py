from ursina import *

# The code is written as, when you run it and press any key, the pressed key will be displayed on the screen.

app = Ursina(development_mode=False, use_ingame_console=True)
key_display = Text('Press any key...', color=color.white, scale=2)

def input(key):
    key_display.text = f'Key pressed: {key}'

app.run()