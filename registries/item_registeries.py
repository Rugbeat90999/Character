from registers import ItemCategory, WearableItem, UsableItem, GeneralItem
from registries.part_registeries import Parts
from registries.registry_registeries import *




IRON_GEAR = ItemCategory().set_name("Iron Gear").set_description("Iron gear from all item types").register("IRON_GEAR", ITEMS)
ARMOR = ItemCategory().set_name("Armor").set_description("Armor type wearable items").register("ARMOR", ITEMS)
WEAPONS = ItemCategory().set_name("Weapons").set_description("Weapon type usable items").register("WEAPONS", ITEMS)


IRON_HELMET = WearableItem().set_name("Iron Helmet").set_description("A simple helmet made of Iron").set_value(1225).set_weight(20).add_wear_location(A_PARTS.bodies.ARMOR_HEAD).set_slash_rating(10).set_pierce_rating(10).set_bludgeon_rating(10).register("IRON_HELMET", ITEMS)
IRON_CHESTPLATE = WearableItem().set_name("Iron Chestplate").set_description("A simple chestplate made of Iron").set_value(1832).set_weight(50).add_wear_location(A_PARTS.bodies.ARMOR_CHEST).set_slash_rating(15).set_pierce_rating(15).set_bludgeon_rating(15).register("IRON_CHESTPLATE", ITEMS)
IRON_LEGGINGS = WearableItem().set_name("Iron Pants").set_description("Simple leggings made of Iron").set_value(1732).set_weight(43).add_wear_location(A_PARTS.bodies.ARMOR_CHEST).set_slash_rating(13).set_pierce_rating(13).set_bludgeon_rating(13).register("IRON_LEGGINGS", ITEMS)
IRON_BOOTS = WearableItem().set_name("Iron Boots").set_description("A simple pair boots made of Iron").set_value(1250).set_weight(18).add_wear_location(A_PARTS.bodies.ARMOR_CHEST).set_slash_rating(11).set_pierce_rating(11).set_bludgeon_rating(11).register("IRON_BOOTS", ITEMS)
IRON_GAUNTLETS = WearableItem().set_name("Iron Gauntlets").set_description("A simple pair of gauntlets made of Iron").set_value(1018).set_weight(10).add_wear_location(A_PARTS.bodies.ARMOR_CHEST).set_slash_rating(9).set_pierce_rating(9).set_bludgeon_rating(9).register("IRON_GAUNTLETS", ITEMS)


IRON_DAGGER = UsableItem().set_name("Iron Dagger").set_description("A simple dagger made of Iron").set_value(1000).set_weight(2).set_durability_type(2).set_grippers_needed(1).set_slash_damage(5).set_pierce_damage(10).set_bludgeon_damage(2).register("IRON_DAGGER", ITEMS)
IRON_MACE = UsableItem().set_name("Iron Mace").set_description("A mace made of Iron").set_value(1034).set_weight(4).set_slash_damage(2).set_durability_type(2).set_grippers_needed(1).set_pierce_damage(1).set_bludgeon_damage(10).register("IRON_MACE", ITEMS)
IRON_SWORD = UsableItem().set_name("Iron Sword").set_description("A simple sword made of Iron").set_value(1200).set_weight(5).set_durability_type(2).set_grippers_needed(1).set_slash_damage(20).set_pierce_damage(15).set_bludgeon_damage(8).register("IRON_SWORD", ITEMS)
IRON_BATTLE_AXE = UsableItem().set_name("Iron Battle Axe").set_description("A battle axe mace made of Iron").set_value(1250).set_weight(12).set_durability_type(2).set_grippers_needed(1).set_slash_damage(10).set_pierce_damage(2).set_bludgeon_damage(1).register("IRON_BATTLE_AXE", ITEMS)
IRON_GREAT_SWORD = UsableItem().set_name("Iron Great Sword").set_description("A simple great sword made of Iron").set_value(1350).set_weight(10).set_durability_type(2).set_grippers_needed(2).set_slash_damage(30).set_pierce_damage(3).set_bludgeon_damage(15).register("IRON_GREAT_SWORD", ITEMS)
IRON_WAR_AXE = UsableItem().set_name("Iron War Axe").set_description("A simple war axe made of Iron").set_value(1425).set_weight(18).set_durability_type(2).set_grippers_needed(2).set_slash_damage(23).set_pierce_damage(5).set_bludgeon_damage(20).register("IRON_WAR_AXE", ITEMS)
IRON_WAR_HAMMER = UsableItem().set_name("Iron War Hammer").set_description("A simple hammer axe made of Iron").set_value(1682).set_weight(25).set_durability_type(2).set_grippers_needed(2).set_slash_damage(3).set_pierce_damage(8).set_bludgeon_damage(30).register("IRON_WAR_HAMMER", ITEMS)

IRON_SHIELD = UsableItem().set_name("Iron Shield").set_description("A simple shield made of Iron").set_value(1100).set_weight(10).set_durability_type(2).set_grippers_needed(1).set_slash_rating(5).set_pierce_rating(5).set_bludgeon_rating(5).register("IRON_SHIELD", ITEMS)


COIN = GeneralItem().set_name("Coin").set_description("A coin").set_value(1).register("COIN", ITEMS)
COINS = GeneralItem().set_name("Coin Stack").set_description("A stack coins").set_value(1).register("COINS", ITEMS)

BOOK = GeneralItem().set_name("Book").set_description("A simple book").set_value(20).register("BOOK", ITEMS)