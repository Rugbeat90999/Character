from CommonLib.classes import UUID
from registers import Effects, EffectCategory, InstantEffect, TemporaryEffect, PermanentEffect
from LocalLibrary import UUIDCounter


c = UUIDCounter(7916)



EffectCategory(UUID(f"{c}")).set_name("Healing").set_description("All healing effects").register("HEALING")
EffectCategory(UUID(f"{c}")).set_name("Damaging").set_description("All offensive effects").register("DAMAGING")
EffectCategory(UUID(f"{c}")).set_name("Buffs").set_description("All buffs").register("BUFF")
EffectCategory(UUID(f"{c}")).set_name("Debuffs").set_description("All buffs").register("DEBUFF")
EffectCategory(UUID(f"{c}")).set_name("Special").set_description("All special effects").register("SPECIAL")


InstantEffect(UUID(f"{c.next_type()}")).add_name("Minor Damage").add_description("Damage health by 10").add_catagory(Effects.Catagories.DAMAGING).add_minor_effect("damage", "health", 10).register("MINOR_DAMAGE")
InstantEffect(UUID(f"{c}")).add_name("Lesser Damage").add_description("Damage health by 20").add_catagory(Effects.Catagories.DAMAGING).add_minor_effect("damage", "health", 20).register("LESSER_DAMAGE")
InstantEffect(UUID(f"{c}")).add_name("Common Damage").add_description("Damage health by 40").add_catagory(Effects.Catagories.DAMAGING).add_minor_effect("damage", "health", 40).register("COMMON_DAMAGE")
InstantEffect(UUID(f"{c}")).add_name("Greater Damage").add_description("Damage health by 80").add_catagory(Effects.Catagories.DAMAGING).add_minor_effect("damage", "health", 80).register("GREATER_DAMAGE")
InstantEffect(UUID(f"{c}")).add_name("Grand Damage").add_description("Damage health by 160").add_catagory(Effects.Catagories.DAMAGING).add_minor_effect("damage", "health", 160).register("GRAND_DAMAGE")

InstantEffect(UUID(f"{c.next_buff_type()}")).add_name("Minor Heal").add_description("Heals 10 health").add_catagory(Effects.Catagories.HEALING).add_minor_effect("heal", "health", 10).register("MINOR_HEAL")
InstantEffect(UUID(f"{c}")).add_name("Lesser Heal").add_description("Heals 20 health").add_catagory(Effects.Catagories.HEALING).add_minor_effect("heal", "health", 20).register("LESSER_HEAL")
InstantEffect(UUID(f"{c}")).add_name("Common Heal").add_description("Heals 40 health").add_catagory(Effects.Catagories.HEALING).add_minor_effect("heal", "health", 40).register("COMMON_HEAL")
InstantEffect(UUID(f"{c}")).add_name("Greater Heal").add_description("Heals 80 health").add_catagory(Effects.Catagories.HEALING).add_minor_effect("heal", "health", 80).register("GREATER_HEAL")
InstantEffect(UUID(f"{c}")).add_name("Grand Heal").add_description("Heals 160 health").add_catagory(Effects.Catagories.HEALING).add_minor_effect("heal", "health", 160).register("GRAND_HEAL")


TemporaryEffect(UUID((f"{c.next_type()}"))).add_name("Minor Poisen").add_description("Damage health by 1 every second").add_catagory(Effects.Catagories.DEBUFF).add_minor_effect("poison", "health", 1).register("MINOR_POISEN")
TemporaryEffect(UUID((f"{c}"))).add_name("Lesser Poisen").add_description("Damage health by 2 every second").add_catagory(Effects.Catagories.DEBUFF).add_minor_effect("poison", "health", 2).register("LESSER_POISEN")
TemporaryEffect(UUID((f"{c}"))).add_name("Common Poisen").add_description("Damage health by 4 every second").add_catagory(Effects.Catagories.DEBUFF).add_minor_effect("poison", "health", 4).register("COMMON_POISEN")
TemporaryEffect(UUID((f"{c}"))).add_name("Greater Poisen").add_description("Damage health by 8 every second").add_catagory(Effects.Catagories.DEBUFF).add_minor_effect("poison", "health", 8).register("GREATER_POISEN")
TemporaryEffect(UUID((f"{c}"))).add_name("Grand Poisen").add_description("Damage health by 16 every second").add_catagory(Effects.Catagories.DEBUFF).add_minor_effect("poison", "health", 16).register("GRAND_POISEN")

TemporaryEffect(UUID((f"{c.next_buff_type()}"))).add_name("Minor Regen").add_description("Regens 1 health every second").add_catagory(Effects.Catagories.BUFF).add_minor_effect("regen", "health", 1).register("MINOR_REGEN")
TemporaryEffect(UUID((f"{c}"))).add_name("Lesser Regen").add_description("Regens 2 health every second").add_catagory(Effects.Catagories.BUFF).add_minor_effect("regen", "health", 2).register("LESSER_REGEN")
TemporaryEffect(UUID((f"{c}"))).add_name("Common Regen").add_description("Regens 4 health every second").add_catagory(Effects.Catagories.BUFF).add_minor_effect("regen", "health", 4).register("COMMON_REGEN")
TemporaryEffect(UUID((f"{c}"))).add_name("Greater Regen").add_description("Regens 8 health every second").add_catagory(Effects.Catagories.BUFF).add_minor_effect("regen", "health", 8).register("GREATER_REGEN")
TemporaryEffect(UUID((f"{c}"))).add_name("Grand Regen").add_description("Regens 16 health every second").add_catagory(Effects.Catagories.BUFF).add_minor_effect("regen", "health", 16).register("GRAND_REGEN")

TemporaryEffect(UUID((f"{c.next_minor_type()}"))).add_name("Minor Weaken").add_description("Decrease max health by 10 for the duration").add_catagory(Effects.Catagories.DEBUFF).add_minor_effect("weaken", "max_health", 10).register("MINOR_WEAKEN")
TemporaryEffect(UUID((f"{c}"))).add_name("Lesser Weaken").add_description("Decrease max health by 20 for the duration").add_catagory(Effects.Catagories.DEBUFF).add_minor_effect("weaken", "max_health", 20).register("LESSER_WEAKEN")
TemporaryEffect(UUID((f"{c}"))).add_name("Common Weaken").add_description("Decrease max health by 40 for the duration").add_catagory(Effects.Catagories.DEBUFF).add_minor_effect("weaken", "max_health", 40).register("COMMON_WEAKEN")
TemporaryEffect(UUID((f"{c}"))).add_name("Greater Weaken").add_description("Decrease max health by 80 for the duration").add_catagory(Effects.Catagories.DEBUFF).add_minor_effect("weaken", "max_health", 80).register("GREATER_WEAKEN")
TemporaryEffect(UUID((f"{c}"))).add_name("Grand Weaken").add_description("Decrease max health by 160 for the duration").add_catagory(Effects.Catagories.DEBUFF).add_minor_effect("weaken", "max_health", 160).register("GRAND_WEAKEN")

TemporaryEffect(UUID((f"{c.next_buff_type()}"))).add_name("Minor Boost").add_description("Boosts max health by 10 for the duration").add_catagory(Effects.Catagories.BUFF).add_minor_effect("boost", "health", 10).register("MINOR_BOOST")
TemporaryEffect(UUID((f"{c}"))).add_name("Lesser Boost").add_description("Boosts max health by 20 for the duration").add_catagory(Effects.Catagories.BUFF).add_minor_effect("boost", "health", 20).register("LESSER_BOOST")
TemporaryEffect(UUID((f"{c}"))).add_name("Common Boost").add_description("Boosts max health by 40 for the duration").add_catagory(Effects.Catagories.BUFF).add_minor_effect("boost", "health", 40).register("COMMON_BOOST")
TemporaryEffect(UUID((f"{c}"))).add_name("Greater Boost").add_description("Boosts max health by 80 for the duration").add_catagory(Effects.Catagories.BUFF).add_minor_effect("boost", "health", 80).register("GREATER_BOOST")
TemporaryEffect(UUID((f"{c}"))).add_name("Grand Boost").add_description("Boosts max health by 160 for the duration").add_catagory(Effects.Catagories.BUFF).add_minor_effect("boost", "health", 160).register("GRAND_BOOST")


PermanentEffect(UUID((f"{c.next_type()}"))).add_name("Minor Cripple").add_description("Decrease max health by 10").add_catagory(Effects.Catagories.DEBUFF).add_minor_effect("weaken", "max_health", 10).register("MINOR_CRIPPLE")
PermanentEffect(UUID((f"{c}"))).add_name("Lesser Cripple").add_description("Decrease max health by 20").add_catagory(Effects.Catagories.DEBUFF).add_minor_effect("weaken", "max_health", 20).register("LESSER_CRIPPLE")
PermanentEffect(UUID((f"{c}"))).add_name("Common Cripple").add_description("Decrease max health by 40").add_catagory(Effects.Catagories.DEBUFF).add_minor_effect("weaken", "max_health", 40).register("COMMON_CRIPPLE")
PermanentEffect(UUID((f"{c}"))).add_name("Greater Cripple").add_description("Decrease max health by 80").add_catagory(Effects.Catagories.DEBUFF).add_minor_effect("weaken", "max_health", 80).register("GREATER_CRIPPLE")
PermanentEffect(UUID((f"{c}"))).add_name("Grand Cripple").add_description("Decrease max health by 160").add_catagory(Effects.Catagories.DEBUFF).add_minor_effect("weaken", "max_health", 160).register("GRAND_CRIPPLE")

PermanentEffect(UUID((f"{c.next_buff_type()}"))).add_name("Minor Boost").add_description("Boosts max health by 10").add_catagory(Effects.Catagories.BUFF).add_minor_effect("boost", "health", 10).register("MINOR_BOOST")
PermanentEffect(UUID((f"{c}"))).add_name("Lesser Boost").add_description("Boosts max health by 20").add_catagory(Effects.Catagories.BUFF).add_minor_effect("boost", "health", 20).register("LESSER_BOOST")
PermanentEffect(UUID((f"{c}"))).add_name("Common Boost").add_description("Boosts max health by 40").add_catagory(Effects.Catagories.BUFF).add_minor_effect("boost", "health", 40).register("COMMON_BOOST")
PermanentEffect(UUID((f"{c}"))).add_name("Greater Boost").add_description("Boosts max health by 80").add_catagory(Effects.Catagories.BUFF).add_minor_effect("boost", "health", 80).register("GREATER_BOOST")
PermanentEffect(UUID((f"{c}"))).add_name("Grand Boost").add_description("Boosts max health by 160").add_catagory(Effects.Catagories.BUFF).add_minor_effect("boost", "health", 160).register("GRAND_BOOST")

PermanentEffect(UUID((f"{c.next_minor_type()}"))).add_name("Lycanthropey").add_description("Changes the effected into a werewolf").add_catagory(Effects.Catagories.SPECIAL).add_minor_effect("lycanthropey").register("LYCANTHROPEY")