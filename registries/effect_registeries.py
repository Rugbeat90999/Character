from registers import EffectCategory, InstantEffect, TemporaryEffect, PermanentEffect
from registries.registry_registeries import *



HEALING = EffectCategory().set_name("Healing").set_description("All healing effects").register("HEALING", EFFECTS)
DAMAGING = EffectCategory().set_name("Damaging").set_description("All offensive effects").register("DAMAGING", EFFECTS)
BUFF = EffectCategory().set_name("Buffs").set_description("All buffs").register("BUFF", EFFECTS)
DEBUFF = EffectCategory().set_name("Debuffs").set_description("All buffs").register("DEBUFF", EFFECTS)
SPECIAL = EffectCategory().set_name("Special").set_description("All special effects").register("SPECIAL", EFFECTS)


MINOR_DAMAGE = InstantEffect().set_name("Minor Damage").set_description("Damage health by 10").add_minor_effect("damage", "health", 10).register("MINOR_DAMAGE", EFFECTS)
LESSER_DAMAGE = InstantEffect().set_name("Lesser Damage").set_description("Damage health by 20").add_minor_effect("damage", "health", 20).register("LESSER_DAMAGE", EFFECTS)
COMMON_DAMAGE = InstantEffect().set_name("Common Damage").set_description("Damage health by 40").add_minor_effect("damage", "health", 40).register("COMMON_DAMAGE", EFFECTS)
GREATER_DAMAGE = InstantEffect().set_name("Greater Damage").set_description("Damage health by 80").add_minor_effect("damage", "health", 80).register("GREATER_DAMAGE", EFFECTS)
GRAND_DAMAGE = InstantEffect().set_name("Grand Damage").set_description("Damage health by 160").add_minor_effect("damage", "health", 160).register("GRAND_DAMAGE", EFFECTS)

MINOR_HEAL = InstantEffect().set_name("Minor Heal").set_description("Heals 10 health").add_minor_effect("heal", "health", 10).register("MINOR_HEAL", EFFECTS)
LESSER_HEAL = InstantEffect().set_name("Lesser Heal").set_description("Heals 20 health").add_minor_effect("heal", "health", 20).register("LESSER_HEAL", EFFECTS)
COMMON_HEAL = InstantEffect().set_name("Common Heal").set_description("Heals 40 health").add_minor_effect("heal", "health", 40).register("COMMON_HEAL", EFFECTS)
GREATER_HEAL = InstantEffect().set_name("Greater Heal").set_description("Heals 80 health").add_minor_effect("heal", "health", 80).register("GREATER_HEAL", EFFECTS)
GRAND_HEAL = InstantEffect().set_name("Grand Heal").set_description("Heals 160 health").add_minor_effect("heal", "health", 160).register("GRAND_HEAL", EFFECTS)


MINOR_POISEN = TemporaryEffect().set_name("Minor Poisen").set_description("Damage health by 1 every second").add_minor_effect("poison", "health", 1).register("MINOR_POISEN", EFFECTS)
LESSER_POISEN = TemporaryEffect().set_name("Lesser Poisen").set_description("Damage health by 2 every second").add_minor_effect("poison", "health", 2).register("LESSER_POISEN", EFFECTS)
COMMON_POISEN = TemporaryEffect().set_name("Common Poisen").set_description("Damage health by 4 every second").add_minor_effect("poison", "health", 4).register("COMMON_POISEN", EFFECTS)
GREATER_POISEN = TemporaryEffect().set_name("Greater Poisen").set_description("Damage health by 8 every second").add_minor_effect("poison", "health", 8).register("GREATER_POISEN", EFFECTS)
GRAND_POISEN = TemporaryEffect().set_name("Grand Poisen").set_description("Damage health by 16 every second").add_minor_effect("poison", "health", 16).register("GRAND_POISEN", EFFECTS)

MINOR_REGEN = TemporaryEffect().set_name("Minor Regen").set_description("Regens 1 health every second").add_minor_effect("regen", "health", 1).register("MINOR_REGEN", EFFECTS)
LESSER_REGEN = TemporaryEffect().set_name("Lesser Regen").set_description("Regens 2 health every second").add_minor_effect("regen", "health", 2).register("LESSER_REGEN", EFFECTS)
COMMON_REGEN = TemporaryEffect().set_name("Common Regen").set_description("Regens 4 health every second").add_minor_effect("regen", "health", 4).register("COMMON_REGEN", EFFECTS)
GREATER_REGEN = TemporaryEffect().set_name("Greater Regen").set_description("Regens 8 health every second").add_minor_effect("regen", "health", 8).register("GREATER_REGEN", EFFECTS)
GRAND_REGEN = TemporaryEffect().set_name("Grand Regen").set_description("Regens 16 health every second").add_minor_effect("regen", "health", 16).register("GRAND_REGEN", EFFECTS)

MINOR_WEAKEN = TemporaryEffect().set_name("Minor Weaken").set_description("Decrease max health by 10 for the duration").add_minor_effect("weaken", "max_health", 10).register("MINOR_WEAKEN", EFFECTS)
LESSER_WEAKEN = TemporaryEffect().set_name("Lesser Weaken").set_description("Decrease max health by 20 for the duration").add_minor_effect("weaken", "max_health", 20).register("LESSER_WEAKEN", EFFECTS)
COMMON_WEAKEN = TemporaryEffect().set_name("Common Weaken").set_description("Decrease max health by 40 for the duration").add_minor_effect("weaken", "max_health", 40).register("COMMON_WEAKEN", EFFECTS)
GREATER_WEAKEN = TemporaryEffect().set_name("Greater Weaken").set_description("Decrease max health by 80 for the duration").add_minor_effect("weaken", "max_health", 80).register("GREATER_WEAKEN", EFFECTS)
GRAND_WEAKEN = TemporaryEffect().set_name("Grand Weaken").set_description("Decrease max health by 160 for the duration").add_minor_effect("weaken", "max_health", 160).register("GRAND_WEAKEN", EFFECTS)

MINOR_BOOST = TemporaryEffect().set_name("Minor Boost").set_description("Boosts max health by 10 for the duration").add_minor_effect("boost", "health", 10).register("MINOR_BOOST", EFFECTS)
LESSER_BOOST = TemporaryEffect().set_name("Lesser Boost").set_description("Boosts max health by 20 for the duration").add_minor_effect("boost", "health", 20).register("LESSER_BOOST", EFFECTS)
COMMON_BOOST = TemporaryEffect().set_name("Common Boost").set_description("Boosts max health by 40 for the duration").add_minor_effect("boost", "health", 40).register("COMMON_BOOST", EFFECTS)
GREATER_BOOST = TemporaryEffect().set_name("Greater Boost").set_description("Boosts max health by 80 for the duration").add_minor_effect("boost", "health", 80).register("GREATER_BOOST", EFFECTS)
GRAND_BOOST = TemporaryEffect().set_name("Grand Boost").set_description("Boosts max health by 160 for the duration").add_minor_effect("boost", "health", 160).register("GRAND_BOOST", EFFECTS)


MINOR_CRIPPLE = PermanentEffect().set_name("Minor Cripple").set_description("Decrease max health by 10").add_minor_effect("weaken", "max_health", 10).register("MINOR_CRIPPLE", EFFECTS)
LESSER_CRIPPLE = PermanentEffect().set_name("Lesser Cripple").set_description("Decrease max health by 20").add_minor_effect("weaken", "max_health", 20).register("LESSER_CRIPPLE", EFFECTS)
COMMON_CRIPPLE = PermanentEffect().set_name("Common Cripple").set_description("Decrease max health by 40").add_minor_effect("weaken", "max_health", 40).register("COMMON_CRIPPLE", EFFECTS)
GREATER_CRIPPLE = PermanentEffect().set_name("Greater Cripple").set_description("Decrease max health by 80").add_minor_effect("weaken", "max_health", 80).register("GREATER_CRIPPLE", EFFECTS)
GRAND_CRIPPLE = PermanentEffect().set_name("Grand Cripple").set_description("Decrease max health by 160").add_minor_effect("weaken", "max_health", 160).register("GRAND_CRIPPLE", EFFECTS)

MINOR_ENHANCE = PermanentEffect().set_name("Minor Boost").set_description("Boosts max health by 10").add_minor_effect("boost", "health", 10).register("MINOR_ENHANCE", EFFECTS)
LESSER_ENHANCE = PermanentEffect().set_name("Lesser Boost").set_description("Boosts max health by 20").add_minor_effect("boost", "health", 20).register("LESSER_ENHANCE", EFFECTS)
COMMON_ENHANCE = PermanentEffect().set_name("Common Boost").set_description("Boosts max health by 40").add_minor_effect("boost", "health", 40).register("COMMON_ENHANCE", EFFECTS)
GREATER_ENHANCE = PermanentEffect().set_name("Greater Boost").set_description("Boosts max health by 80").add_minor_effect("boost", "health", 80).register("GREATER_ENHANCE", EFFECTS)
GRAND_ENHANCE = PermanentEffect().set_name("Grand Boost").set_description("Boosts max health by 160").add_minor_effect("boost", "health", 160).register("GRAND_ENHANCE", EFFECTS)

LYCANTHROPEY = PermanentEffect().set_name("Lycanthropey").set_description("Changes the effected into a werewolf").add_minor_effect("lycanthropey").register("LYCANTHROPEY", EFFECTS)