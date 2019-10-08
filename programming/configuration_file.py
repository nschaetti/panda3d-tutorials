
# ConfigVariableManager.getGlobalPtr().listVariables()
import sys
from panda3d.core import ConfigVariableString, ConfigVariableManager

my_game_server = ConfigVariableString('my-game-server', '127.0.0.1')
print('Server specified in config file: ', my_game_server.getValue())

# Allow the user to change servers on the command-line
if sys.argv[1] == '--server':
    my_game_server.setValue(sys.argv[2])
# end if

print('Server that we will user: ', my_game_server.getValue())

print(ConfigVariableString("my-game-server"))

cvMgr = ConfigVariableManager.get_global_ptr()
cvMgr.list_variables()
