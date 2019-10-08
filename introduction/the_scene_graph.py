
from math import pi, sin, cos
from direct.showbase.ShowBase import ShowBase
from direct.task import Task


class MyApp(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)

        # Load the environment model.
        self.scene = self.loader.loadModel("models/environment")

        # Reparent the model to render
        self.scene.reparentTo(self.render)

        # Apply scale and position transforms on the model
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8, 42, 0)

        # Add the spinCameraTask procedure to the task manager.
        self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")
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
