
from math import pi, sin, cos
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import Point3


class MyApp(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)

        # Disable the camera trackball controls
        self.disableMouse()

        # Load the environment model.
        self.scene = self.loader.loadModel("models/environment")

        # Reparent the model to render
        self.scene.reparentTo(self.render)

        # Apply scale and position transforms on the model
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8, 42, 0)

        # Add the spinCameraTask procedure to the task manager.
        self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")

        # Load and transform the panda actor
        self.panda_actor = Actor("models/panda-model", {"walk": "models/panda-walk4"})
        self.panda_actor.setScale(0.005, 0.005, 0.005)
        self.panda_actor.reparentTo(self.render)

        # Loop animation
        self.panda_actor.loop("walk")

        # Create the four lerp intervals needed for the panda to
        # walk back and forth.
        pandaPosInterval1 = self.panda_actor.posInterval(13, Point3(0, -10, 0), startPos=Point3(0, 10, 0))
        pandaPosInterval2 = self.panda_actor.posInterval(13, Point3(0, 10, 0), startPos=Point3(0, -10, 0))
        pandaHprInterval1 = self.panda_actor.hprInterval(3, Point3(180, 0, 0), startHpr=Point3(0, 0, 0))
        pandaHprInterval2 = self.panda_actor.hprInterval(3, Point3(0, 0, 0), startHpr=Point3(180, 0, 0))

        # Create and play the sequence that coordinates the intervals.
        self.pandaPace = Sequence(pandaPosInterval1, pandaHprInterval1, pandaPosInterval2, pandaHprInterval2)

        # Loop
        self.pandaPace.loop()
    # end __init__

    # Define a procedure to move the camera
    def spinCameraTask(self, task):
        angle_degree = task.time * 6.0
        angle_radians = angle_degree * (pi / 180.0)
        self.camera.setPos(20 * sin(angle_radians), -20.0 * cos(angle_radians), 3)
        self.camera.setHpr(angle_degree, 0, 0)
        return Task.cont
    # end spinCameraTask

# end MyApp

# Run
app = MyApp()
app.run()
