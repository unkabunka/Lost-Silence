''''https://www.youtube.com/watch?v=QtzuxPUJ_Qc = Panda3D game prototype - used this as reference
 - second reference'''
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
from panda3d.core import DirectionalLight
from panda3d.core import loadPrcFile
from panda3d.core import AmbientLight
loadPrcFile('settings.prc') # Loads the settings file so that I can cache the models for better loading and so it doesn't look all blurry



class Game(ShowBase):
    def __init__(self):
        super().__init__()
        self.LoadModels()
        self.LoadLights()

    def LoadTerrarin(self):
        pass
    def LoadModels(self):
          self.tile = loader.loadModel("dirt-block.glb")
          self.tile.reparentTo(render)

    def LoadLights(self):
        self.mainLight = DirectionalLight("main light")
        self.mainLightNodePath = render.attachNewNode(self.mainLight)
        self.mainLightNodePath.setHpr(30, -60, 0) #stands for heading (side to side camera), pitch (up to down camera), roll
        self.render.setLight(self.mainLightNodePath) #renders the light to the scene so it actually works

        self.ambientLight = AmbientLight("ambient light") #so that some parts of the model aren't pitch black and so there still are shadows but they're not too dark
        self.ambientLight.setColor((0.2, 0.2, 0.2, 1)) #the 1 at the end is for alpha/transparency
        self.ambientLightNodePath = render.attachNewNode(self.ambientLight)
        self.render.setLight(self.ambientLightNodePath)
        
if __name__ == "__main__":
    g = Game()
    g.run()