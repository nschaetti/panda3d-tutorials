
import sys, os
import direct.directbase.DirectStart
from panda3d.core import Filename

# Get the location of the 'py' file
mydir = os.path.abspath(sys.path[0])

# Loading
m = loader.loadModel(mydir + "/models/mymodel.egg")
