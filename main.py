''''This is simply a test, please don't grade it or consider it a part of the assignment because im just trying to get a player sprite that i can control into this thingie majingie'''
'''
class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # Load the environment model.
        self.scene = self.loader.loadModel("models/environment")
        # Reparent the model to render.
        self.scene.reparentTo(self.render)
        # Apply scale and position transforms on the model.
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8, 42, 0)

        # Add the spinCameraTask procedure to the task manager.
        self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")

        # Load and transform the panda actor.
        self.pandaActor = Actor("models/panda-model",
                                {"walk": "models/panda-walk4"})
        self.pandaActor.setScale(0.005, 0.005, 0.005)
        self.pandaActor.reparentTo(self.render)
        # Loop its animation.
        self.pandaActor.loop("walk")

    # Define a procedure to move the camera.
    def spinCameraTask(self, task):
        angleDegrees = task.time * 6.0
        angleRadians = angleDegrees * (pi / 180.0)
        self.camera.setPos(20 * sin(angleRadians), -20 * cos(angleRadians), 3)
        self.camera.setHpr(angleDegrees, 0, 0)
        return Task.cont


app = MyApp()
app.run()
'''
from panda3d.core import loadPrcFileData
loadPrcFileData('', 'window-title Aniketh Nandipatis Awesome Game!!!!1!!1!!')
import direct.directbase.DirectStart
from panda3d.core import WindowProperties
from panda3d.core import CollisionTraverser,CollisionNode
from panda3d.core import CollisionHandlerQueue,CollisionRay
from panda3d.core import CollisionTube,CollisionSegment
from panda3d.core import Filename,AmbientLight,DirectionalLight
from panda3d.core import PandaNode,NodePath,Camera,TextNode
from panda3d.core import Point3,Vec3,Vec4,BitMask32
from panda3d.core import LightRampAttrib
from direct.gui.OnscreenText import OnscreenText
from direct.actor.Actor import Actor
from direct.showbase.DirectObject import DirectObject
import random, sys, os, math
from direct.showbase.ShowBase import ShowBase
from settings import *

class Game(ShowBase, DirectObject):
    def __init__(self):
        super().__init__()
        #working on camera controls today:
        self.controlMap = {"left":0, "right":0, "forward":0, "backward":0}
        self.mousebtn = [0,0,0]
        self.disable_mouse()
        #loads a basic cube to the environment by using loader and the model is from ShowBase
        test_cube = self.loader.loadModel("models/box")
        #sets the position of the cube
        test_cube.setPos(-10, 10, 0)
        #reparents the cube to the render so that it shows up in the game window
        test_cube.reparentTo(self.render)

        #loads a panda model to the environment
        panda_actor = self.loader.loadModel("models/panda-model")
        #scales down the panda model so that it fits in the window
        panda_actor.setScale(0.005)
        #sets the position of the panda model
        panda_actor.setPos(10, 10, 0)
        #reparents the panda model to the render so that it shows up in the game window
        panda_actor.reparentTo(self.render)

game = Game()
game.run()