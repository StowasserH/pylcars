from .gui import Gui
from .widgets import Widgets
#from .enumeration import Enumeration
from .conditions import Conditions
from .colors import Colors
from .orientation import Orientation

def joke():
    return (u'SELECT * FROM joke ORDER BY RAND() DESC')
