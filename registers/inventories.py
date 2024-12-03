from define import Inventory
from registers import tags



BASE_STASH = Inventory(50, "STASH", "Stash")
BASE_EQUIPPMENT = Inventory(5, "EQUIPPMENT", "Equippment")
BASE_TRINKETS = Inventory(22, "TRINKETS", "Trinkets")
BASE_USABLE = Inventory(6, "USABLE", "Usable")
BASE_ACTIVE = Inventory(2, "ACTIVE", "Active")






BASE_TRINKETS[0]["slot_name"] = "face"
BASE_TRINKETS[0]["tags"] = [tags.TRINKETS_FACE]
BASE_TRINKETS[1]["slot_name"] = "Left Ear"
BASE_TRINKETS[1]["tags"] = [tags.TRINKETS_EAR]
BASE_TRINKETS[2]["slot_name"] = "Right Ear"
BASE_TRINKETS[2]["tags"] = [tags.TRINKETS_EAR]
BASE_TRINKETS[3]["slot_name"] = "neck"
BASE_TRINKETS[3]["tags"] = [tags.TRINKETS_NECK]
BASE_TRINKETS[4]["slot_name"] = "cape"
BASE_TRINKETS[4]["tags"] = [tags.TRINKETS_CAPE]
BASE_TRINKETS[5]["slot_name"] = "Left Wrist"
BASE_TRINKETS[5]["tags"] = [tags.TRINKETS_WRIST]
BASE_TRINKETS[6]["slot_name"] = "Right Wrist"
BASE_TRINKETS[6]["tags"] = [tags.TRINKETS_WRIST]
BASE_TRINKETS[7]["slot_name"] = "Left Hand"
BASE_TRINKETS[7]["tags"] = [tags.TRINKETS_HAND]
BASE_TRINKETS[8]["slot_name"] = "Right Hand"
BASE_TRINKETS[8]["tags"] = [tags.TRINKETS_HAND]

start = 9
hands = 2
fingers = 5


for j in range(hands):
 index = (j * fingers) + start
 for k in range(fingers):
   jndex = k + index
   BASE_TRINKETS[jndex]["slot_name"] = f"finger_{j+1}_{k+1}"
   BASE_TRINKETS[jndex]["tags"] = [tags.TRINKETS_FINGER]


BASE_TRINKETS[19]["slot_name"] = "Belt"
BASE_TRINKETS[19]["tags"] = [tags.TRINKETS_BELT]
BASE_TRINKETS[20]["slot_name"] = "Left Ankle"
BASE_TRINKETS[20]["tags"] = [tags.TRINKETS_ANKLE]
BASE_TRINKETS[21]["slot_name"] = "right Ankle"
BASE_TRINKETS[21]["tags"] = [tags.TRINKETS_ANKLE]


BASE_EQUIPPMENT[0]["slot_name"] = "head"
BASE_EQUIPPMENT[0]["tags"] = [tags.ARMOR_HEAD]
BASE_EQUIPPMENT[1]["slot_name"] = "body"
BASE_EQUIPPMENT[1]["tags"] = [tags.ARMOR_BODY]
BASE_EQUIPPMENT[2]["slot_name"] = "hands"
BASE_EQUIPPMENT[2]["tags"] = [tags.ARMOR_HANDS]
BASE_EQUIPPMENT[3]["slot_name"] = "legs"
BASE_EQUIPPMENT[3]["tags"] = [tags.ARMOR_LEGS]
BASE_EQUIPPMENT[4]["slot_name"] = "feet"
BASE_EQUIPPMENT[4]["tags"] = [tags.ARMOR_FEET]

BASE_USABLE[0]["slot_name"] = "Right Shoulder"
BASE_USABLE[0]["tags"] = [tags.HEAVY, tags.MASSIVE]
BASE_USABLE[1]["slot_name"] = "Left Shoulder"
BASE_USABLE[1]["tags"] = [tags.HEAVY, tags.MASSIVE]
BASE_USABLE[2]["slot_name"] = "Right Hip"
BASE_USABLE[2]["tags"] = [tags.MEDIUM, tags.LIGHT]
BASE_USABLE[3]["slot_name"] = "Left Hip"
BASE_USABLE[3]["tags"] = [tags.MEDIUM, tags.LIGHT]
BASE_USABLE[4]["slot_name"] = "Right Thigh"
BASE_USABLE[4]["tags"] = [tags.LIGHT]
BASE_USABLE[5]["slot_name"] = "Left Thigh"
BASE_USABLE[5]["tags"] = [tags.LIGHT]



BASE_ACTIVE[0]["slot_name"] = "Right Hand"
BASE_ACTIVE[0]["tags"] = [tags.USABLE]
BASE_ACTIVE[1]["slot_name"] = "Left Hand"
BASE_ACTIVE[1]["tags"] = [tags.USABLE]




HUMAN = [BASE_STASH.copy("STASH", "Stash"), BASE_EQUIPPMENT.copy("EQUIPPMENT", "Equippment"), BASE_TRINKETS.copy("TRINKETS", "Trinkets"), BASE_USABLE.copy("USABLE", "Usable"), BASE_ACTIVE.copy("ACTIVE", "Active")]
ELF = [BASE_STASH.copy("STASH", "Stash"), BASE_EQUIPPMENT.copy("EQUIPPMENT", "Equippment"), BASE_TRINKETS.copy("TRINKETS", "Trinkets"), BASE_USABLE.copy("USABLE", "Usable"), BASE_ACTIVE.copy("ACTIVE", "Active")]
DWARF = [BASE_STASH.copy("STASH", "Stash"), BASE_EQUIPPMENT.copy("EQUIPPMENT", "Equippment"), BASE_TRINKETS.copy("TRINKETS", "Trinkets"), BASE_USABLE.copy("USABLE", "Usable"), BASE_ACTIVE.copy("ACTIVE", "Active")]
ORC = [BASE_STASH.copy("STASH", "Stash"), BASE_EQUIPPMENT.copy("EQUIPPMENT", "Equippment"), BASE_TRINKETS.copy("TRINKETS", "Trinkets"), BASE_USABLE.copy("USABLE", "Usable"), BASE_ACTIVE.copy("ACTIVE", "Active")]
KITSUNE = [BASE_STASH.copy("STASH", "Stash"), BASE_EQUIPPMENT.copy("EQUIPPMENT", "Equippment"), BASE_TRINKETS.copy("TRINKETS", "Trinkets"), BASE_USABLE.copy("USABLE", "Usable"), BASE_ACTIVE.copy("ACTIVE", "Active")]
KOBOLD = [BASE_STASH.copy("STASH", "Stash"), BASE_EQUIPPMENT.copy("EQUIPPMENT", "Equippment"), BASE_TRINKETS.copy("TRINKETS", "Trinkets"), BASE_USABLE.copy("USABLE", "Usable"), BASE_ACTIVE.copy("ACTIVE", "Active")]



for i in [HUMAN, ELF, DWARF, ORC]:
  i[3].add_slot(6)
  i[3][6]["slot_name"] = "Lower Back"
  i[3][6]["tags"] = [tags.RANGED]


start = 22
tails = 9


for i in range(tails):
  KITSUNE[2][i]["slot_name"] = f"tail_{i+1}"
  KITSUNE[2][i]["tags"] = [tags.TRINKETS_TAIL]


KOBOLD[2][i]["slot_name"] = f"tail"
KOBOLD[2][i]["tags"] = [tags.TRINKETS_TAIL]