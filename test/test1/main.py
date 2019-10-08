# Imports
import sys
import direct.directbase.DirectStart
from direct.showbase.DirectObject import DirectObject
from panda3d.core import AmbientLight
from panda3d.core import DirectionalLight
from panda3d.core import Vec3
from panda3d.core import Vec4


# RoboticLab
class RoboticLab(DirectObject):
    """
    RoboticLab
    """

    # Constructor
    def __init__(self):
        # Base
        base.set_background_color(0.2, 0.2, 0.2, 1)
        base.set_frame_rate_meter(True)
        base.cam.set_pos(0, -20, 4)
        base.cam.look_at(0, 0, 0)

        # Light 1
        light1 = AmbientLight('ambientLight')
        light1.set_color(Vec4(0.5, 0.5, 0.5, 1.0))
        light1_node_path = render.attach_new_node(light1)

        # Light 2
        light2 = DirectionalLight('directionalLight')
        light2.set_direction(Vec3(1, 1, -1))
        light2.set_color(Vec4(0.7, 0.7, 0.7, 1))
        light2_node_path = render.attach_new_node(light2)

        # Clear light
        render.clear_light()
        render.set_light(light1_node_path)
        render.set_light(light2_node_path)

        # Input
        self.accept('escape', self.exit_lab())

        # Input state
        inputState.watchWithModifiers('forward', 'w')

        # Task
        taskMgr.add(self._update, 'updateWorld')

        # Physics
        self.setup()
    # end __init__

    #############################
    # PRIVATE
    #############################

    # Process input
    def processInput(self, dt):
        """
        Process input
        :param dt:
        :return:
        """
        print("processInput")
    # end processInput

    # Clean up
    def _cleanup(self):
        """
        Clean up
        :return:
        """
        pass
    # end _cleanup

    # Update the scene
    def _update(self):
        """
        Update the scene
        :return:
        """
        # Delta time
        dt = globalClock.getDt()

        # Continue
        return task.cont
    # end _update

    #############################
    # EVENTS
    #############################

    # Exit lab
    def exit_lab(self):
        """
        Exit lab
        :return:
        """
        self._cleanup()
        sys.exit(1)
    # end exit_lab

# end RoboticLab

# Run
robotic_lab = RoboticLab()
run()
