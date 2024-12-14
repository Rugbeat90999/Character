from define import Race
from registers import inventories

ELF = Race("ELF", inventories.ELF, [None]).register()
DWARF = Race("DWARF", inventories.DWARF, [None]).register()
HUMAN = Race("HUMAN", inventories.HUMAN, [None]).register()
ORC = Race("ORC", inventories.ORC, [None]).register()
KITSUNE = Race("KITSUNE", inventories.KITSUNE, [None]).register()
KOBOLD = Race("KOBOLD", inventories.KOBOLD, [None]).register()
# DRAGON = Race("DRAGON", inventories.DRAGON, [None])
# TINY = Race("TINY", inventories.TINY, [None])
# GIANT = Race("GIANT", inventories.GIANT, [None])
# PIXIE = Race("PIXIE", inventories.PIXIE, [None])
# FAIRY = Race("FAIRY", inventories.FAIRY, [None])
# SPRITE = Race("SPRITE", inventories.SPRITE, [None])
# IMP = Race("IMP", inventories.IMP, [None])
# GNOME = Race("GNOME", inventories.GNOME, [None])
# GOBLIN = Race("GOBLIN", inventories.GOBLIN, [None])
# TROLL = Race("TROLL", inventories.TROLL, [None])