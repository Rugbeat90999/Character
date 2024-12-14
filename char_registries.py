from registers import *
import define
from define import Character
from CommonLib.classes import Path, UUID


ME = Character(Path("./char_data/me.char"), "ME").register()
ME2 = Character(Path("./char_data/me copy.char"), "ME2").register()