from registers import Effects, EffectCategory, InstantEffect, TemporaryEffect, PermanentEffect




EffectCategory().set_name("Healing").set_description("All healing effects").register("HEALING")
EffectCategory().set_name("Damaging").set_description("All offensive effects").register("DAMAGING")
EffectCategory().set_name("Buffs").set_description("All buffs").register("BUFF")
EffectCategory().set_name("Debuffs").set_description("All buffs").register("DEBUFF")
EffectCategory().set_name("Special").set_description("All special effects").register("SPECIAL")


InstantEffect().set_name("Minor Damage").set_description("Damage health by 10").add_catagory(Effects.Catagories.DAMAGING).add_minor_effect("damage", "health", 10).register("MINOR_DAMAGE")
InstantEffect().set_name("Lesser Damage").set_description("Damage health by 20").add_catagory(Effects.Catagories.DAMAGING).add_minor_effect("damage", "health", 20).register("LESSER_DAMAGE")
InstantEffect().set_name("Common Damage").set_description("Damage health by 40").add_catagory(Effects.Catagories.DAMAGING).add_minor_effect("damage", "health", 40).register("COMMON_DAMAGE")
InstantEffect().set_name("Greater Damage").set_description("Damage health by 80").add_catagory(Effects.Catagories.DAMAGING).add_minor_effect("damage", "health", 80).register("GREATER_DAMAGE")
InstantEffect().set_name("Grand Damage").set_description("Damage health by 160").add_catagory(Effects.Catagories.DAMAGING).add_minor_effect("damage", "health", 160).register("GRAND_DAMAGE")

InstantEffect().set_name("Minor Heal").set_description("Heals 10 health").add_catagory(Effects.Catagories.HEALING).add_minor_effect("heal", "health", 10).register("MINOR_HEAL")
InstantEffect().set_name("Lesser Heal").set_description("Heals 20 health").add_catagory(Effects.Catagories.HEALING).add_minor_effect("heal", "health", 20).register("LESSER_HEAL")
InstantEffect().set_name("Common Heal").set_description("Heals 40 health").add_catagory(Effects.Catagories.HEALING).add_minor_effect("heal", "health", 40).register("COMMON_HEAL")
InstantEffect().set_name("Greater Heal").set_description("Heals 80 health").add_catagory(Effects.Catagories.HEALING).add_minor_effect("heal", "health", 80).register("GREATER_HEAL")
InstantEffect().set_name("Grand Heal").set_description("Heals 160 health").add_catagory(Effects.Catagories.HEALING).add_minor_effect("heal", "health", 160).register("GRAND_HEAL")


TemporaryEffect().set_name("Minor Poisen").set_description("Damage health by 1 every second").add_catagory(Effects.Catagories.DEBUFF).add_minor_effect("poison", "health", 1).register("MINOR_POISEN")
TemporaryEffect().set_name("Lesser Poisen").set_description("Damage health by 2 every second").add_catagory(Effects.Catagories.DEBUFF).add_minor_effect("poison", "health", 2).register("LESSER_POISEN")
TemporaryEffect().set_name("Common Poisen").set_description("Damage health by 4 every second").add_catagory(Effects.Catagories.DEBUFF).add_minor_effect("poison", "health", 4).register("COMMON_POISEN")
TemporaryEffect().set_name("Greater Poisen").set_description("Damage health by 8 every second").add_catagory(Effects.Catagories.DEBUFF).add_minor_effect("poison", "health", 8).register("GREATER_POISEN")
TemporaryEffect().set_name("Grand Poisen").set_description("Damage health by 16 every second").add_catagory(Effects.Catagories.DEBUFF).add_minor_effect("poison", "health", 16).register("GRAND_POISEN")

TemporaryEffect().set_name("Minor Regen").set_description("Regens 1 health every second").add_catagory(Effects.Catagories.BUFF).add_minor_effect("regen", "health", 1).register("MINOR_REGEN")
TemporaryEffect().set_name("Lesser Regen").set_description("Regens 2 health every second").add_catagory(Effects.Catagories.BUFF).add_minor_effect("regen", "health", 2).register("LESSER_REGEN")
TemporaryEffect().set_name("Common Regen").set_description("Regens 4 health every second").add_catagory(Effects.Catagories.BUFF).add_minor_effect("regen", "health", 4).register("COMMON_REGEN")
TemporaryEffect().set_name("Greater Regen").set_description("Regens 8 health every second").add_catagory(Effects.Catagories.BUFF).add_minor_effect("regen", "health", 8).register("GREATER_REGEN")
TemporaryEffect().set_name("Grand Regen").set_description("Regens 16 health every second").add_catagory(Effects.Catagories.BUFF).add_minor_effect("regen", "health", 16).register("GRAND_REGEN")

TemporaryEffect().set_name("Minor Weaken").set_description("Decrease max health by 10 for the duration").add_catagory(Effects.Catagories.DEBUFF).add_minor_effect("weaken", "max_health", 10).register("MINOR_WEAKEN")
TemporaryEffect().set_name("Lesser Weaken").set_description("Decrease max health by 20 for the duration").add_catagory(Effects.Catagories.DEBUFF).add_minor_effect("weaken", "max_health", 20).register("LESSER_WEAKEN")
TemporaryEffect().set_name("Common Weaken").set_description("Decrease max health by 40 for the duration").add_catagory(Effects.Catagories.DEBUFF).add_minor_effect("weaken", "max_health", 40).register("COMMON_WEAKEN")
TemporaryEffect().set_name("Greater Weaken").set_description("Decrease max health by 80 for the duration").add_catagory(Effects.Catagories.DEBUFF).add_minor_effect("weaken", "max_health", 80).register("GREATER_WEAKEN")
TemporaryEffect().set_name("Grand Weaken").set_description("Decrease max health by 160 for the duration").add_catagory(Effects.Catagories.DEBUFF).add_minor_effect("weaken", "max_health", 160).register("GRAND_WEAKEN")

TemporaryEffect().set_name("Minor Boost").set_description("Boosts max health by 10 for the duration").add_catagory(Effects.Catagories.BUFF).add_minor_effect("boost", "health", 10).register("MINOR_BOOST")
TemporaryEffect().set_name("Lesser Boost").set_description("Boosts max health by 20 for the duration").add_catagory(Effects.Catagories.BUFF).add_minor_effect("boost", "health", 20).register("LESSER_BOOST")
TemporaryEffect().set_name("Common Boost").set_description("Boosts max health by 40 for the duration").add_catagory(Effects.Catagories.BUFF).add_minor_effect("boost", "health", 40).register("COMMON_BOOST")
TemporaryEffect().set_name("Greater Boost").set_description("Boosts max health by 80 for the duration").add_catagory(Effects.Catagories.BUFF).add_minor_effect("boost", "health", 80).register("GREATER_BOOST")
TemporaryEffect().set_name("Grand Boost").set_description("Boosts max health by 160 for the duration").add_catagory(Effects.Catagories.BUFF).add_minor_effect("boost", "health", 160).register("GRAND_BOOST")


PermanentEffect().set_name("Minor Cripple").set_description("Decrease max health by 10").add_catagory(Effects.Catagories.DEBUFF).add_minor_effect("weaken", "max_health", 10).register("MINOR_CRIPPLE")
PermanentEffect().set_name("Lesser Cripple").set_description("Decrease max health by 20").add_catagory(Effects.Catagories.DEBUFF).add_minor_effect("weaken", "max_health", 20).register("LESSER_CRIPPLE")
PermanentEffect().set_name("Common Cripple").set_description("Decrease max health by 40").add_catagory(Effects.Catagories.DEBUFF).add_minor_effect("weaken", "max_health", 40).register("COMMON_CRIPPLE")
PermanentEffect().set_name("Greater Cripple").set_description("Decrease max health by 80").add_catagory(Effects.Catagories.DEBUFF).add_minor_effect("weaken", "max_health", 80).register("GREATER_CRIPPLE")
PermanentEffect().set_name("Grand Cripple").set_description("Decrease max health by 160").add_catagory(Effects.Catagories.DEBUFF).add_minor_effect("weaken", "max_health", 160).register("GRAND_CRIPPLE")

PermanentEffect().set_name("Minor Boost").set_description("Boosts max health by 10").add_catagory(Effects.Catagories.BUFF).add_minor_effect("boost", "health", 10).register("MINOR_BOOST")
PermanentEffect().set_name("Lesser Boost").set_description("Boosts max health by 20").add_catagory(Effects.Catagories.BUFF).add_minor_effect("boost", "health", 20).register("LESSER_BOOST")
PermanentEffect().set_name("Common Boost").set_description("Boosts max health by 40").add_catagory(Effects.Catagories.BUFF).add_minor_effect("boost", "health", 40).register("COMMON_BOOST")
PermanentEffect().set_name("Greater Boost").set_description("Boosts max health by 80").add_catagory(Effects.Catagories.BUFF).add_minor_effect("boost", "health", 80).register("GREATER_BOOST")
PermanentEffect().set_name("Grand Boost").set_description("Boosts max health by 160").add_catagory(Effects.Catagories.BUFF).add_minor_effect("boost", "health", 160).register("GRAND_BOOST")

PermanentEffect().set_name("Lycanthropey").set_description("Changes the effected into a werewolf").add_catagory(Effects.Catagories.SPECIAL).add_minor_effect("lycanthropey").register("LYCANTHROPEY")