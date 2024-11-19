from define import Inventory
from registers.tags import *




STASH = Inventory(50, "STASH", "Stash")
EQUIPPMENT = Inventory(5, "EQUIPPMENT", "Equippment")
TRINKETS = Inventory(22, "TRINKETS", "Trinkets")
USABLE = Inventory(7, "USABLE", "Usable")
ACTIVE = Inventory(2, "ACTIVE", "Active")




HUMAN = [STASH, EQUIPPMENT, TRINKETS, USABLE, ACTIVE]




HUMAN[2][0]["slot_name"] = "face"
HUMAN[2][0]["tags"] = [TAG_TRINKETS_FACE]
HUMAN[2][1]["slot_name"] = "Left Ear"
HUMAN[2][1]["tags"] = [TAG_TRINKETS_EAR]
HUMAN[2][2]["slot_name"] = "Right Ear"
HUMAN[2][2]["tags"] = [TAG_TRINKETS_EAR]
HUMAN[2][3]["slot_name"] = "neck"
HUMAN[2][3]["tags"] = [TAG_TRINKETS_NECK]
HUMAN[2][4]["slot_name"] = "cape"
HUMAN[2][4]["tags"] = [TAG_TRINKETS_CAPE]
HUMAN[2][5]["slot_name"] = "Left Wrist"
HUMAN[2][5]["tags"] = [TAG_TRINKETS_WRIST]
HUMAN[2][6]["slot_name"] = "Right Wrist"
HUMAN[2][6]["tags"] = [TAG_TRINKETS_WRIST]
HUMAN[2][7]["slot_name"] = "Left Hand"
HUMAN[2][7]["tags"] = [TAG_TRINKETS_HAND]
HUMAN[2][8]["slot_name"] = "Right Hand"
HUMAN[2][8]["tags"] = [TAG_TRINKETS_HAND]

start = 9
hands = 2
fingers = 5

for i in range(hands):
  index = (i * fingers) + start
  for j in range(fingers):
    jndex = j + index
    HUMAN[2][jndex]["slot_name"] = f"finger_{i+1}_{j+1}"
    HUMAN[2][jndex]["tags"] = [TAG_TRINKETS_FINGER]


HUMAN[2][19]["slot_name"] = "Belt"
HUMAN[2][19]["tags"] = [TAG_TRINKETS_BELT]
HUMAN[2][20]["slot_name"] = "Left Ankle"
HUMAN[2][20]["tags"] = [TAG_TRINKETS_ANKLE]
HUMAN[2][21]["slot_name"] = "right Ankle"
HUMAN[2][21]["tags"] = [TAG_TRINKETS_ANKLE]


HUMAN[1][0]["slot_name"] = "head"
HUMAN[1][0]["tags"] = [TAG_ARMOR_HEAD]
HUMAN[1][1]["slot_name"] = "body"
HUMAN[1][1]["tags"] = [TAG_ARMOR_BODY]
HUMAN[1][2]["slot_name"] = "hands"
HUMAN[1][2]["tags"] = [TAG_ARMOR_HANDS]
HUMAN[1][3]["slot_name"] = "legs"
HUMAN[1][3]["tags"] = [TAG_ARMOR_LEGS]
HUMAN[1][4]["slot_name"] = "feet"
HUMAN[1][4]["tags"] = [TAG_ARMOR_FEET]

HUMAN[3][0]["slot_name"] = "Right Shoulder"
HUMAN[3][0]["tags"] = [TAG_HEAVY, TAG_MASSIVE]
HUMAN[3][1]["slot_name"] = "Left Shoulder"
HUMAN[3][1]["tags"] = [TAG_HEAVY, TAG_MASSIVE]
HUMAN[3][2]["slot_name"] = "Right Hip"
HUMAN[3][2]["tags"] = [TAG_MEDIUM]
HUMAN[3][3]["slot_name"] = "Left Hip"
HUMAN[3][3]["tags"] = [TAG_MEDIUM]
HUMAN[3][4]["slot_name"] = "Right Thigh"
HUMAN[3][4]["tags"] = [TAG_LIGHT]
HUMAN[3][5]["slot_name"] = "Left Thigh"
HUMAN[3][5]["tags"] = [TAG_LIGHT]
HUMAN[3][6]["slot_name"] = "Lower Back"
HUMAN[3][6]["tags"] = [TAG_BOW]


HUMAN[4][0]["slot_name"] = "Right Hand"
HUMAN[4][0]["tags"] = [TAG_USABLE]
HUMAN[4][1]["slot_name"] = "Left Hand"
HUMAN[4][1]["tags"] = [TAG_USABLE]