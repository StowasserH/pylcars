from .gui import gui
from .gui import Conditions
from .gui import Colors

def joke():
    return (u'SELECT * FROM joke ORDER BY RAND() DESC')
