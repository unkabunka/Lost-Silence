''''https://www.youtube.com/watch?v=QtzuxPUJ_Qc = Panda3D game prototype - used this as reference
I ended up giving up on Pandas3D because Ursina is way easier to use and has a lot of built in features that make it better for my use case
but I wanted to keep this code for reference
References for Ursina: https://www.ursinaengine.org/ursina_for_dummies.html'''

from ursina import *                    # Import the ursina engine
import random                           # Import the random library

random_generator = random.Random()      # Create a random number generator

def update():
    cube.rotation_y += time.dt * 100                 # Rotate every time update is called
def input(key):
        if key == 'space':
            red = random_generator.random() * 255
            green = random_generator.random() * 255
            blue = random_generator.random() * 255
            cube.color = color.rgb(red, green, blue)


app = Ursina()                          # Initialise your Ursina app

window.title = 'My Game'                # The window title
window.borderless = False               # Show a border
window.fullscreen = False               # Do not go Fullscreen
window.exit_button.visible = False      # Do not show the in-game red X that loses the window
window.fps_counter.enabled = True       # Show the FPS (Frames per second) counter

cube = Entity(model='cube', color=color.orange, scale=(2,2,2))
app.run() 

app.run()   