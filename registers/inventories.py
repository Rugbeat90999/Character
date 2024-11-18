from define import Inventory

STASH = Inventory(50, "STASH", "Stash")
EQUIPPMENT = Inventory(5, "EQUIPPMENT", "Equippment")
TRINKETS = Inventory(20, "TRINKETS", "Trinkets")
USABLE = Inventory(7, "TOOLS", "Tools")
ACTIVE = Inventory(2, "ACTIVE", "Active")




for i in range(10):
  index = i
  num = i
  num_a = 1
  if i > 4:
    num_a = 2
    num -= 5
  TRINKETS[index]["slot_name"] = f"finger_{num_a}_{num}"
  TRINKETS[index]["tag_list"] = ["finger"]

TRINKETS[10]["slot_name"] = "face"
TRINKETS[10]["tag_list"] = ["wearable/trinket/face"]
TRINKETS[11]["slot_name"] = "neck"
TRINKETS[11]["tag_list"] = ["wearable/trinket/neck"]
TRINKETS[12]["slot_name"] = "cape"
TRINKETS[12]["tag_list"] = ["wearable/trinket/cape"]
TRINKETS[13]["slot_name"] = "belt"
TRINKETS[13]["tag_list"] = ["wearable/trinket/belt"]
TRINKETS[14]["slot_name"] = "Left Wrist"
TRINKETS[14]["tag_list"] = ["wearable/trinket/wrist"]
TRINKETS[15]["slot_name"] = "Right Wrist"
TRINKETS[15]["tag_list"] = ["wearable/trinket/wrist"]
TRINKETS[16]["slot_name"] = "Left Ankle"
TRINKETS[16]["tag_list"] = ["wearable/trinket/ankle"]
TRINKETS[17]["slot_name"] = "right Ankle"
TRINKETS[17]["tag_list"] = ["wearable/trinket/ankle"]
TRINKETS[18]["slot_name"] = "Left Ea/"
TRINKETS[18]["tag_list"] = ["wearable/trinket/ear"]
TRINKETS[19]["slot_name"] = "Right Ear"
TRINKETS[19]["tag_list"] = ["wearable/trinket/ear"]

EQUIPPMENT[0]["slot_name"] = "head"
EQUIPPMENT[0]["tag_list"] = ["armor/head"]
EQUIPPMENT[1]["slot_name"] = "body"
EQUIPPMENT[1]["tag_list"] = ["armor/body"]