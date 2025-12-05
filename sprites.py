from panda3d.core import DirectionalLight
from direct.showbase.ShowBase import ShowBase

class CubeSprite(ShowBase):
    def LoadModels(self):
          self.tile = loader.loadModel("dirt-block.glb")
          self.tile.reparentTo(render)