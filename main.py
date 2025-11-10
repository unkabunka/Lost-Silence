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
from direct.showbase.ShowBase import ShowBase

from direct.actor.Actor import Actor
from panda3d.core import WindowProperties
from panda3d.core import Loader as loader
from panda3d.core import AmbientLight
from panda3d.core import Vec4

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        self.disableMouse()

        properties = WindowProperties()
        properties.setSize(1000, 750)
        self.win.requestProperties(properties)

        self.environment = loader.loadModel("Models/Misc/environment")
        self.environment.reparentTo(render)

        self.tempActor = Actor("Models/PandaChan/act_p3d_chan", {"walk" : "Models/PandaChan/a_p3d_chan_run"})
        self.tempActor.getChild(0).setH(180)
        self.tempActor.reparentTo(render)
        self.tempActor.loop("walk")

        self.camera.setPos(0, 0, 32)
        self.camera.setP(-90)

game = Game()
game.run()