from CommonLib.functions import log
from define import Items


ITEM_REGISTRY = Items(True, True, True)


KNIGHTS_SWORD = ITEM_REGISTRY.add("KNIGHTS_SWORD", "Knight\'s Sword", 20, 130, 1, "A sword commonly used by Knights of the Holard Kingdom")

# Trinkets
RING_OF_FIRE = ITEM_REGISTRY.add("RING_OF_FIRE", "Ring of Fire", 1, 120, 1, "Grants resistance to fire damage.").add_tag("finger")
RING_OF_WATER = ITEM_REGISTRY.add("RING_OF_WATER", "Ring of Water", 1, 110, 1, "Allows breathing underwater.").add_tag("finger")
RING_OF_EARTH = ITEM_REGISTRY.add("RING_OF_EARTH", "Ring of Earth", 1, 100, 1, "Increases defense.").add_tag("finger")
RING_OF_AIR = ITEM_REGISTRY.add("RING_OF_AIR", "Ring of Air", 1, 115, 1, "Boosts agility and speed.").add_tag("finger")
RING_OF_LIFE = ITEM_REGISTRY.add("RING_OF_LIFE", "Ring of Life", 1, 200, 1, "Restores health over time.").add_tag("finger")
RING_OF_PROTECTION = ITEM_REGISTRY.add("RING_OF_PROTECTION", "Ring of Protection", 1, 130, 1, "Increases defense.").add_tag("finger")
RING_OF_HEALTH = ITEM_REGISTRY.add("RING_OF_HEALTH", "Ring of Health", 1, 150, 1, "Slightly boosts max health.").add_tag("finger")
RING_OF_REGENERATION = ITEM_REGISTRY.add("RING_OF_REGENERATION", "Ring of Regeneration", 1, 180, 1, "Gradually restores health over time.").add_tag("finger")
RING_OF_MANA = ITEM_REGISTRY.add("RING_OF_MANA", "Ring of Mana", 1, 140, 1, "Slightly boosts max mana.").add_tag("finger")
RING_OF_THE_ELEMENTS = ITEM_REGISTRY.add("RING_OF_THE_ELEMENTS", "Ring of the Elements", 1, 200, 1, "Increases elemental damage.").add_tag("finger")
RING_OF_FOCUS = ITEM_REGISTRY.add("RING_OF_FOCUS", "Ring of Focus", 1, 120, 1, "Improves accuracy and concentration.").add_tag("finger")
RING_OF_THE_WARRIOR = ITEM_REGISTRY.add("RING_OF_THE_WARRIOR", "Ring of the Warrior", 1, 170, 1, "Enhances physical attack power.").add_tag("finger")
RING_OF_THE_MAGE = ITEM_REGISTRY.add("RING_OF_THE_MAGE", "Ring of the Mage", 1, 160, 1, "Boosts magical damage.").add_tag("finger")
RING_OF_THE_HUNTER = ITEM_REGISTRY.add("RING_OF_THE_HUNTER", "Ring of the Hunter", 1, 140, 1, "Improves ranged attack accuracy.").add_tag("finger")
RING_OF_THE_SPIRIT = ITEM_REGISTRY.add("RING_OF_THE_SPIRIT", "Ring of the Spirit", 1, 190, 1, "Increases spiritual energy and resilience.").add_tag("finger")

MASK_OF_SHADOWS = ITEM_REGISTRY.add("MASK_OF_SHADOWS", "Mask of Shadows", 2, 150, 1, "Hides the wearer in darkness.").add_tag("face")
MASK_OF_TERROR = ITEM_REGISTRY.add("MASK_OF_TERROR", "Mask of Terror", 2, 180, 1, "Intimidates nearby foes.").add_tag("face")
MASK_OF_SMILES = ITEM_REGISTRY.add("MASK_OF_SMILES", "Mask of Smiles", 1, 90, 1, "Charms people around you.").add_tag("face")
MASK_OF_DEATH = ITEM_REGISTRY.add("MASK_OF_DEATH", "Mask of Death", 2, 220, 1, "Increases power but reduces health.").add_tag("face")
MASK_OF_VISION = ITEM_REGISTRY.add("MASK_OF_VISION", "Mask of Vision", 2, 160, 1, "Allows the wearer to see hidden objects.").add_tag("face")

AMULET_OF_POWER = ITEM_REGISTRY.add("AMULET_OF_POWER", "Amulet of Power", 1, 200, 1, "Increases all stats slightly.").add_tag("neck")
AMULET_OF_FORTUNE = ITEM_REGISTRY.add("AMULET_OF_FORTUNE", "Amulet of Fortune", 1, 150, 1, "Increases drop rates for rare items.").add_tag("neck")
PENDANT_OF_MAGIC = ITEM_REGISTRY.add("PENDANT_OF_MAGIC", "Pendant of Magic", 1, 120, 1, "Boosts magical abilities.").add_tag("neck")
NECKLACE_OF_THE_SEA = ITEM_REGISTRY.add("NECKLACE_OF_THE_SEA", "Necklace of the Sea", 1, 130, 1, "Grants water resistance.").add_tag("neck")
NECKLACE_OF_LIGHT = ITEM_REGISTRY.add("NECKLACE_OF_LIGHT", "Necklace of Light", 1, 170, 1, "Increases healing effects.").add_tag("neck")

CAPE_OF_THE_HERO = ITEM_REGISTRY.add("CAPE_OF_THE_HERO", "Cape of the Hero", 3, 250, 1, "Boosts all stats significantly.").add_tag("cape")
CAPE_OF_WINDS = ITEM_REGISTRY.add("CAPE_OF_WINDS", "Cape of Winds", 2, 150, 1, "Allows for faster travel.").add_tag("cape")
CAPE_OF_SHADOWS = ITEM_REGISTRY.add("CAPE_OF_SHADOWS", "Cape of Shadows", 2, 180, 1, "Grants stealth capabilities.").add_tag("cape")
CAPE_OF_FLAMES = ITEM_REGISTRY.add("CAPE_OF_FLAMES", "Cape of Flames", 3, 200, 1, "Increases fire-based attacks.").add_tag("cape")
CAPE_OF_FROST = ITEM_REGISTRY.add("CAPE_OF_FROST", "Cape of Frost", 3, 180, 1, "Grants immunity to freezing effects.").add_tag("cape")

BELT_OF_GIANT_STRENGTH = ITEM_REGISTRY.add("BELT_OF_GIANT_STRENGTH", "Belt of Giant Strength", 2, 180, 1, "Massively increases strength.").add_tag("belt")
BELT_OF_AGILITY = ITEM_REGISTRY.add("BELT_OF_AGILITY", "Belt of Agility", 1, 140, 1, "Improves speed and dexterity.").add_tag("belt")
BELT_OF_ENDURANCE = ITEM_REGISTRY.add("BELT_OF_ENDURANCE", "Belt of Endurance", 2, 160, 1, "Grants extra health and stamina.").add_tag("belt")
BELT_OF_THIEVES = ITEM_REGISTRY.add("BELT_OF_THIEVES", "Belt of Thieves", 1, 120, 1, "Enhances stealth and lockpicking skills.").add_tag("belt")
BELT_OF_TIME = ITEM_REGISTRY.add("BELT_OF_TIME", "Belt of Time", 2, 200, 1, "Slightly slows down time around the wearer.").add_tag("belt")

BRACERS_OF_DEFENSE = ITEM_REGISTRY.add("BRACERS_OF_DEFENSE", "Bracers of Defense", 2, 150, 1, "Boosts physical defense.").add_tag("wrist")
BRACERS_OF_SWIFTNESS = ITEM_REGISTRY.add("BRACERS_OF_SWIFTNESS", "Bracers of Swiftness", 1, 130, 1, "Increases movement speed.").add_tag("wrist")
WRISTBAND_OF_POWER = ITEM_REGISTRY.add("WRISTBAND_OF_POWER", "Wristband of Power", 1, 160, 1, "Enhances melee damage.").add_tag("wrist")
WRISTBAND_OF_GRACE = ITEM_REGISTRY.add("WRISTBAND_OF_GRACE", "Wristband of Grace", 1, 120, 1, "Improves balance and coordination.").add_tag("wrist")
CUFFS_OF_MAGIC = ITEM_REGISTRY.add("CUFFS_OF_MAGIC", "Cuffs of Magic", 2, 170, 1, "Increases magical energy.").add_tag("wrist")

ANKLET_OF_LIGHTNESS = ITEM_REGISTRY.add("ANKLET_OF_LIGHTNESS", "Anklet of Lightness", 1, 80, 1, "Reduces stamina usage while running.").add_tag("ankle")
ANKLET_OF_SWIFTNESS = ITEM_REGISTRY.add("ANKLET_OF_SWIFTNESS", "Anklet of Swiftness", 1, 100, 1, "Increases running speed.").add_tag("ankle")
ANKLET_OF_STABILITY = ITEM_REGISTRY.add("ANKLET_OF_STABILITY", "Anklet of Stability", 1, 90, 1, "Prevents being knocked down.").add_tag("ankle")
ANKLET_OF_GRACE = ITEM_REGISTRY.add("ANKLET_OF_GRACE", "Anklet of Grace", 1, 110, 1, "Improves movement and balance.").add_tag("ankle")
ANKLET_OF_STRENGTH = ITEM_REGISTRY.add("ANKLET_OF_STRENGTH", "Anklet of Strength", 1, 120, 1, "Enhances leg-based strength.").add_tag("ankle")

EARRINGS_OF_INSIGHT = ITEM_REGISTRY.add("EARRINGS_OF_INSIGHT", "Earrings of Insight", 1, 140, 1, "Boosts perception and awareness.").add_tag("ear")
EARRINGS_OF_STRENGTH = ITEM_REGISTRY.add("EARRINGS_OF_STRENGTH", "Earrings of Strength", 1, 120, 1, "Increases physical strength.").add_tag("ear")
EARRINGS_OF_MAGIC = ITEM_REGISTRY.add("EARRINGS_OF_MAGIC", "Earrings of Magic", 1, 150, 1, "Enhances magical abilities.").add_tag("ear")
EARRINGS_OF_FOCUS = ITEM_REGISTRY.add("EARRINGS_OF_FOCUS", "Earrings of Focus", 1, 130, 1, "Improves concentration and accuracy.").add_tag("ear")
EARRINGS_OF_CHARISMA = ITEM_REGISTRY.add("EARRINGS_OF_CHARISMA", "Earrings of Charisma", 1, 110, 1, "Enhances social interactions.").add_tag("ear")

GLOVES_OF_POWER = ITEM_REGISTRY.add("GLOVES_OF_POWER", "Gloves of Power", 2, 150, 1, "Boosts melee attack strength.").add_tag("hand")
GLOVES_OF_MAGIC = ITEM_REGISTRY.add("GLOVES_OF_MAGIC", "Gloves of Magic", 1, 140, 1, "Enhances spellcasting ability.").add_tag("hand")
GLOVES_OF_SWIFTNESS = ITEM_REGISTRY.add("GLOVES_OF_SWIFTNESS", "Gloves of Swiftness", 1, 120, 1, "Increases hand speed and dexterity.").add_tag("hand")
GLOVES_OF_GRIP = ITEM_REGISTRY.add("GLOVES_OF_GRIP", "Gloves of Grip", 1, 100, 1, "Improves grip and handling.").add_tag("hand")
GLOVES_OF_PROTECTION = ITEM_REGISTRY.add("GLOVES_OF_PROTECTION", "Gloves of Protection", 2, 170, 1, "Reduces damage from hand-based attacks.").add_tag("hand")