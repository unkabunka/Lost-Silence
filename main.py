''''https://www.youtube.com/watch?v=QtzuxPUJ_Qc = Panda3D game prototype - used this as my'''
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


from panda3d.core import GeomVertexData, GeomVertexFormat, Geom, GeomTriangles, GeomVertexWriter, GeomNode, Texture, TextureAttrib, NodePath, RenderState, ModelRoot
from direct.showbase.ShowBase import ShowBase

class MyApp(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)

        # Creating vertex data.
        vdata = GeomVertexData('name', GeomVertexFormat.getV3n3t2(), Geom.UHStatic)
        vdata.setNumRows(3)

        vertex = GeomVertexWriter(vdata, 'vertex')
        normal = GeomVertexWriter(vdata, 'normal')
        texcoord = GeomVertexWriter(vdata, 'texcoord')

        # Adding vertex data.
        vertex.addData3(-1, -1, 0)
        vertex.addData3(1, -1, 0)
        vertex.addData3(1, 1, 0)
        vertex.addData3(-1, 1, 0)

        normal.addData3(0, 0, 1)
        normal.addData3(0, 0, 1)
        normal.addData3(0, 0, 1)
        normal.addData3(0, 0, 1)
        
        texcoord.addData2(0, 0)
        texcoord.addData2(1, 0)
        texcoord.addData2(1, 1)
        texcoord.addData2(0, 1)


        # Creating primitive - a.
        prim_a = GeomTriangles(Geom.UHStatic)
        prim_a.addVertices(0, 1, 2)
        prim_a.addVertices(0, 2, 3)
        prim_a.closePrimitive()

        geom1 = Geom(vdata)
        geom1.addPrimitive(prim_a)


        # Load texture.
        tex1 = Texture("Texture")
        tex1.setup2dTexture()
        tex1.read('panda.jpg')
        tex1.setMagfilter(Texture.FTNearest)
        tex1.setMinfilter(Texture.FTNearest)

        # Create new geom state.
        state_a = RenderState.make(TextureAttrib.make(tex1))

        # Create geom node.
        geom_node = GeomNode('Plane')
        geom_node.add_geom(geom1, state_a)

        # Attach geom node.
        root = NodePath(geom_node)
        root.reparent_to(render)
        #root.writeBamFile("plane.bam")

app = MyApp()
app.run()
