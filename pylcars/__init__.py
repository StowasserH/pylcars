from .lcars import Lcars
#from .enumeration import Enumeration
from .conditions import Conditions
from .colors import Colors
from .orientation import Orientation
from .widgets.semicircle import Semicircle
from .widgets.deco import Deco
from .widgets.block import Block
from .widgets.separator import Separator
from .widgets.bracket import Bracket
from .widgets.menue import Menue
from .widgets.updown import Updown
from .sound import Sound

def joke():
    return (u'SELECT * FROM joke ORDER BY RAND() DESC')
