from registers import tags
from define import Item


KNIGHTS_SWORD = Item("KNIGHTS_SWORD").set_weight(20).set_value(130).set_stack_size(1).add_tag(tags.TRINKETS_FACE).register()

# Trinkets
RING_OF_FIRE = Item("RING_OF_FIRE").set_stack_size(1).set_value(120).set_weight(1).add_tag(tags.TRINKETS_FINGER).register()
RING_OF_WATER = Item("RING_OF_WATER").set_stack_size(1).set_value(110).set_weight(1).add_tag(tags.TRINKETS_FINGER).register()
RING_OF_EARTH = Item("RING_OF_EARTH").set_stack_size(1).set_value(100).set_weight(1).add_tag(tags.TRINKETS_FINGER).register()
RING_OF_AIR = Item("RING_OF_AIR").set_stack_size(1).set_value(115).set_weight(1).add_tag(tags.TRINKETS_FINGER).register()
RING_OF_LIFE = Item("RING_OF_LIFE").set_stack_size(1).set_value(200).set_weight(1).add_tag(tags.TRINKETS_FINGER).register()
RING_OF_PROTECTION = Item("RING_OF_PROTECTION").set_stack_size(1).set_value(130).set_weight(1).add_tag(tags.TRINKETS_FINGER).register()
RING_OF_HEALTH = Item("RING_OF_HEALTH").set_stack_size(1).set_value(150).set_weight(1).add_tag(tags.TRINKETS_FINGER).register()
RING_OF_REGENERATION = Item("RING_OF_REGENERATION").set_stack_size(1).set_value(180).set_weight(1).add_tag(tags.TRINKETS_FINGER).register()
RING_OF_MANA = Item("RING_OF_MANA").set_stack_size(1).set_value(140).set_weight(1).add_tag(tags.TRINKETS_FINGER).register()
RING_OF_THE_ELEMENTS = Item("RING_OF_THE_ELEMENTS").set_stack_size(1).set_value(200).set_weight(1).add_tag(tags.TRINKETS_FINGER).register()
RING_OF_FOCUS = Item("RING_OF_FOCUS").set_stack_size(1).set_value(120).set_weight(1).add_tag(tags.TRINKETS_FINGER).register()
RING_OF_THE_WARRIOR = Item("RING_OF_THE_WARRIOR").set_stack_size(1).set_value(170).set_weight(1).add_tag(tags.TRINKETS_FINGER).register()
RING_OF_THE_MAGE = Item("RING_OF_THE_MAGE").set_stack_size(1).set_value(160).set_weight(1).add_tag(tags.TRINKETS_FINGER).register()
RING_OF_THE_HUNTER = Item("RING_OF_THE_HUNTER").set_stack_size(1).set_value(140).set_weight(1).add_tag(tags.TRINKETS_FINGER).register()
RING_OF_THE_SPIRIT = Item("RING_OF_THE_SPIRIT").set_stack_size(1).set_value(190).set_weight(1).add_tag(tags.TRINKETS_FINGER).register()

MASK_OF_SHADOWS = Item("MASK_OF_SHADOWS").set_weight(2).set_value(150).set_stack_size(1).add_tag(tags.TRINKETS_FACE).register()
MASK_OF_TERROR = Item("MASK_OF_TERROR").set_weight(2).set_value(180).set_stack_size(1).add_tag(tags.TRINKETS_FACE).register()
MASK_OF_SMILES = Item("MASK_OF_SMILES").set_weight(1).set_value(90).set_stack_size(1).add_tag(tags.TRINKETS_FACE).register()
MASK_OF_DEATH = Item("MASK_OF_DEATH").set_weight(2).set_value(220).set_stack_size(1).add_tag(tags.TRINKETS_FACE).register()
MASK_OF_VISION = Item("MASK_OF_VISION").set_weight(2).set_value(160).set_stack_size(1).add_tag(tags.TRINKETS_FACE).register()

AMULET_OF_POWER = Item("AMULET_OF_POWER").set_stack_size(1).set_value(200).set_weight(1).add_tag(tags.TRINKETS_NECK).register()
AMULET_OF_FORTUNE = Item("AMULET_OF_FORTUNE").set_stack_size(1).set_value(150).set_weight(1).add_tag(tags.TRINKETS_NECK).register()
PENDANT_OF_MAGIC = Item("PENDANT_OF_MAGIC").set_stack_size(1).set_value(120).set_weight(1).add_tag(tags.TRINKETS_NECK).register()
NECKLACE_OF_THE_SEA = Item("NECKLACE_OF_THE_SEA").set_stack_size(1).set_value(130).set_weight(1).add_tag(tags.TRINKETS_NECK).register()
NECKLACE_OF_LIGHT = Item("NECKLACE_OF_LIGHT").set_stack_size(1).set_value(170).set_weight(1).add_tag(tags.TRINKETS_NECK).register()

CAPE_OF_THE_HERO = Item("CAPE_OF_THE_HERO").set_stack_size(1).set_value(250).set_weight(1).add_tag(tags.TRINKETS_CAPE).register()
CAPE_OF_WINDS = Item("CAPE_OF_WINDS").set_stack_size(1).set_value(150).set_weight(1).add_tag(tags.TRINKETS_CAPE).register()
CAPE_OF_SHADOWS = Item("CAPE_OF_SHADOWS").set_stack_size(1).set_value(180).set_weight(1).add_tag(tags.TRINKETS_CAPE).register()
CAPE_OF_FLAMES = Item("CAPE_OF_FLAMES").set_stack_size(1).set_value(200).set_weight(1).add_tag(tags.TRINKETS_CAPE).register()
CAPE_OF_FROST = Item("CAPE_OF_FROST").set_stack_size(1).set_value(180).set_weight(1).add_tag(tags.TRINKETS_CAPE).register()

BELT_OF_GIANT_STRENGTH = Item("BELT_OF_GIANT_STRENGTH").set_stack_size(1).set_value(180).set_weight(1).add_tag(tags.TRINKETS_BELT).register()
BELT_OF_AGILITY = Item("BELT_OF_AGILITY").set_stack_size(1).set_value(140).set_weight(1).add_tag(tags.TRINKETS_BELT).register()
BELT_OF_ENDURANCE = Item("BELT_OF_ENDURANCE").set_stack_size(1).set_value(160).set_weight(1).add_tag(tags.TRINKETS_BELT).register()
BELT_OF_THIEVES = Item("BELT_OF_THIEVES").set_stack_size(1).set_value(120).set_weight(1).add_tag(tags.TRINKETS_BELT).register()
BELT_OF_TIME = Item("BELT_OF_TIME").set_stack_size(1).set_value(200).set_weight(1).add_tag(tags.TRINKETS_BELT).register()

BRACERS_OF_DEFENSE = Item("BRACERS_OF_DEFENSE").set_stack_size(1).set_value(150).set_weight(1).add_tag(tags.TRINKETS_WRIST).register()
BRACERS_OF_SWIFTNESS = Item("BRACERS_OF_SWIFTNESS").set_stack_size(1).set_value(130).set_weight(1).add_tag(tags.TRINKETS_WRIST).register()
WRISTBAND_OF_POWER = Item("WRISTBAND_OF_POWER").set_stack_size(1).set_value(160).set_weight(1).add_tag(tags.TRINKETS_WRIST).register()
WRISTBAND_OF_GRACE = Item("WRISTBAND_OF_GRACE").set_stack_size(1).set_value(120).set_weight(1).add_tag(tags.TRINKETS_WRIST).register()
CUFFS_OF_MAGIC = Item("CUFFS_OF_MAGIC").set_stack_size(1).set_value(170).set_weight(1).add_tag(tags.TRINKETS_WRIST).register()

ANKLET_OF_LIGHTNESS = Item("ANKLET_OF_LIGHTNESS").set_stack_size(1).set_value(80).set_weight(1).add_tag(tags.TRINKETS_ANKLE).register()
ANKLET_OF_SWIFTNESS = Item("ANKLET_OF_SWIFTNESS").set_stack_size(1).set_value(100).set_weight(1).add_tag(tags.TRINKETS_ANKLE).register()
ANKLET_OF_STABILITY = Item("ANKLET_OF_STABILITY").set_stack_size(1).set_value(90).set_weight(1).add_tag(tags.TRINKETS_ANKLE).register()
ANKLET_OF_GRACE = Item("ANKLET_OF_GRACE").set_stack_size(1).set_value(110).set_weight(1).add_tag(tags.TRINKETS_ANKLE).register()
ANKLET_OF_STRENGTH = Item("ANKLET_OF_STRENGTH").set_stack_size(1).set_value(120).set_weight(1).add_tag(tags.TRINKETS_ANKLE).register()

EARRINGS_OF_INSIGHT = Item("EARRINGS_OF_INSIGHT").set_stack_size(1).set_value(140).set_weight(1).add_tag(tags.TRINKETS_EAR).register()
EARRINGS_OF_STRENGTH = Item("EARRINGS_OF_STRENGTH").set_stack_size(1).set_value(120).set_weight(1).add_tag(tags.TRINKETS_EAR).register()
EARRINGS_OF_MAGIC = Item("EARRINGS_OF_MAGIC").set_stack_size(1).set_value(150).set_weight(1).add_tag(tags.TRINKETS_EAR).register()
EARRINGS_OF_FOCUS = Item("EARRINGS_OF_FOCUS").set_stack_size(1).set_value(130).set_weight(1).add_tag(tags.TRINKETS_EAR).register()
EARRINGS_OF_CHARISMA = Item("EARRINGS_OF_CHARISMA").set_stack_size(1).set_value(110).set_weight(1).add_tag(tags.TRINKETS_EAR).register()

GLOVES_OF_POWER = Item("GLOVES_OF_POWER").set_stack_size(1).set_value(150).set_weight(1).add_tag(tags.TRINKETS_HAND).register()
GLOVES_OF_MAGIC = Item("GLOVES_OF_MAGIC").set_stack_size(1).set_value(140).set_weight(1).add_tag(tags.TRINKETS_HAND).register()
GLOVES_OF_SWIFTNESS = Item("GLOVES_OF_SWIFTNESS").set_stack_size(1).set_value(120).set_weight(1).add_tag(tags.TRINKETS_HAND).register()
GLOVES_OF_GRIP = Item("GLOVES_OF_GRIP").set_stack_size(1).set_value(100).set_weight(1).add_tag(tags.TRINKETS_HAND).register()
GLOVES_OF_PROTECTION = Item("GLOVES_OF_PROTECTION").set_stack_size(1).set_value(170).set_weight(1).add_tag(tags.TRINKETS_HAND).register()
