from registers import ItemCategory, WearableItem, UsableItem, GeneralItem
from registries.body_location_registeries import BodyLocation
from CommonLib.classes import UUID
from LocalLibrary import UUIDCounter


c = UUIDCounter(7916)


ItemCategory(UUID(f"{c}")).set_name("Iron Gear").set_description("Iron gear from all item types").register("IRON_GEAR")
ItemCategory(UUID(f"{c}")).set_name("Armor").set_description("Armor type wearable items").register("ARMOR")
ItemCategory(UUID(f"{c}")).set_name("Weapons").set_description("Weapon type usable items").register("WEAPONS")


WearableItem(UUID(f"{c.next_type()}")).set_name("Iron Helmet").set_description("A simple helmet made of Iron").set_value(1225).set_weight(20).add_body_location(BodyLocation.ARMOR_HEAD).set_slash_rating(10).set_pierce_rating(10).set_bludgeon_rating(10).register("IRON_HELMET")
WearableItem(UUID(f"{c.next_buff_type()}")).set_name("Iron Chestplate").set_description("A simple chestplate made of Iron").set_value(1832).set_weight(50).add_body_location(BodyLocation.ARMOR_CHEST).set_slash_rating(15).set_pierce_rating(15).set_bludgeon_rating(15).register("IRON_CHESTPLATE")
WearableItem(UUID(f"{c.next_buff_type()}")).set_name("Iron Pants").set_description("Simple leggings made of Iron").set_value(1732).set_weight(43).add_body_location(BodyLocation.ARMOR_CHEST).set_slash_rating(13).set_pierce_rating(13).set_bludgeon_rating(13).register("IRON_LEGGINGS")
WearableItem(UUID(f"{c.next_buff_type()}")).set_name("Iron Boots").set_description("A simple pair boots made of Iron").set_value(1250).set_weight(18).add_body_location(BodyLocation.ARMOR_CHEST).set_slash_rating(11).set_pierce_rating(11).set_bludgeon_rating(11).register("IRON_BOOTS")
WearableItem(UUID(f"{c.next_buff_type()}")).set_name("Iron Gauntlets").set_description("A simple pair of gauntlets made of Iron").set_value(1018).set_weight(10).add_body_location(BodyLocation.ARMOR_CHEST).set_slash_rating(9).set_pierce_rating(9).set_bludgeon_rating(9).register("IRON_GAUNTLETS")

UsableItem(UUID(f"{c.next_type()}")).set_name("Iron Sword").set_description("A simple sword made of Iron").set_value(1425).set_weight(15).set_slash_damage(25).set_pierce_damage(0).set_bludgeon_damage(0).register("IRON_SWORD")
UsableItem(UUID(f"{c.next_buff_type()}")).set_name("Iron Shield").set_description("A simple shield made of Iron").set_value(1100).set_weight(10).set_slash_rating(5).set_pierce_rating(5).set_bludgeon_rating(5).register("IRON_SHIELD")
