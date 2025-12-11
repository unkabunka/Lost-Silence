from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from perlin_noise import PerlinNoise
from numpy import floor
from random import randint

app = Ursina()

terrain = Entity(model = None, collider = None)
noise = PerlinNoise(octaves = 2, seed = randint(-1000000000,1000000000))

terrain_width = 20
freq = 24
amp = 5

window.color = color.rgb(0,0,0)
indra = Sky()
indra.color = window.color
window.fullscreen = True

for i in range(terrain_width*terrain_width):
    cube = Entity(model = 'cube', collider = 'mesh', texture = 'white_cube')
    cube.x = floor(i / terrain_width)
    cube.z = floor(i % terrain_width)
    cube.y = floor(noise([cube.x / freq, cube.z / freq]) * amp)

class Voxel(Button):
    def __init__(self, position=(0,0,0)):
        super().__init__(parent=scene,
            position=position,
            model='cube',
            origin_y=.5,
            texture='white_cube',
            color=color.hsv(0, 0, random.uniform(.9, 1.0)),
            highlight_color=color.lime,
        )
        
player = FirstPersonController()

def input(key):
    if key == 'left mouse down':
        hit_info = raycast(camera.world_position, camera.forward, distance=5)
        if hit_info.hit:
            Voxel(position=hit_info.entity.position + hit_info.normal)
    if key == 'right mouse down' and mouse.hovered_entity:
        destroy(mouse.hovered_entity)
    if held_keys['r']:
        print('r for sprint')
        player.speed = 10
    else:
        player.speed = 5
    if key == 'escape':
        application.quit()

app.run()
