''''https://www.youtube.com/watch?v=QtzuxPUJ_Qc = Panda3D game prototype - used this as reference
I ended up giving up on Pandas3D because Ursina is way easier to use and has a lot of built in features that make it better for my use case
but I wanted to keep this code for reference
References for Ursina: https://www.ursinaengine.org/ursina_for_dummies.html'''

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import math
import random

app = Ursina()

# Window settings
window.title = 'Ursina Voxel Demo (no textures)'
window.borderless = False
window.fullscreen = False
window.exit_button.visible = True
window.fps_counter.enabled = True

# Lighting
DirectionalLight(y=2, z=3, shadows=True)
AmbientLight(color=Vec4(0.6, 0.6, 0.6, 1))

# Simple palette (no textures)
GRASS = color.rgb(106, 190, 48)
DIRT  = color.rgb(134, 96, 67)
STONE = color.rgb(120, 120, 120)
SAND  = color.rgb(237, 201, 175)
WATER = color.rgb(64, 164, 223)

palette = {
    'grass': GRASS,
    'dirt' : DIRT,
    'stone': STONE,
    'sand' : SAND,
    'water': WATER
}

# Voxel class
class Voxel(Button):
    def __init__(self, position=(0,0,0), texture=None, color=color.white, **kwargs):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            origin_y=0.5,
            texture=None,        # we don't use textures
            color=color,
            scale=1,
            collider='box',
            **kwargs
        )

    def input(self, key):
        # left click -> remove
        if self.hovered:
            if key == 'left mouse down':
                destroy(self)
            if key == 'right mouse down':
                # place a block adjacent to this one
                new_pos = self.position + mouse.normal
                # prevent placing blocks inside the player
                if not (player.position - new_pos).length() < 0.9:
                    Voxel(position=new_pos, color=current_block_color)

# Controls UI text
instructions = Text(
    text="Left click: remove block   •   Right click: place block   •   Scroll: change block color",
    origin=(0, -15),
    background=True,
    scale=1.25
)
