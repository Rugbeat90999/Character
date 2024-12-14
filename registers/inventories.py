from define import Inventory
from registers import tags


BASE_STASH = Inventory(50, "STASH")
BASE_EQUIPPMENT = Inventory(5, "EQUIPPMENT")
BASE_TRINKETS = Inventory(22, "TRINKETS")
BASE_USABLE = Inventory(6, "USABLE")
BASE_ACTIVE = Inventory(2, "ACTIVE")




BASE_TRINKETS.slots[0].set_name("face")
BASE_TRINKETS.slots[0].add_tag(tags.TRINKETS_FACE)
BASE_TRINKETS.slots[1].set_name("left_ear")
BASE_TRINKETS.slots[1].add_tag(tags.TRINKETS_EAR)
BASE_TRINKETS.slots[2].set_name("right_ear")
BASE_TRINKETS.slots[2].add_tag(tags.TRINKETS_EAR)
BASE_TRINKETS.slots[3].set_name("neck")
BASE_TRINKETS.slots[3].add_tag(tags.TRINKETS_NECK)
BASE_TRINKETS.slots[4].set_name("cape")
BASE_TRINKETS.slots[4].add_tag(tags.TRINKETS_CAPE)
BASE_TRINKETS.slots[5].set_name("left_wrist")
BASE_TRINKETS.slots[5].add_tag(tags.TRINKETS_WRIST)
BASE_TRINKETS.slots[6].set_name("right_wrist")
BASE_TRINKETS.slots[6].add_tag(tags.TRINKETS_WRIST)
BASE_TRINKETS.slots[7].set_name("left_hand")
BASE_TRINKETS.slots[7].add_tag(tags.TRINKETS_HAND)
BASE_TRINKETS.slots[8].set_name("right_hand")
BASE_TRINKETS.slots[8].add_tag(tags.TRINKETS_HAND)


start = 9
hands = 2
fingers = 5


for i in range(hands):
 index = (i * fingers) + start
 for j in range(fingers):
   jndex = j + index
   BASE_TRINKETS.slots[jndex].set_name(f"finger_{i+1}_{j+1}")
   BASE_TRINKETS.slots[jndex].add_tag(tags.TRINKETS_FINGER)


BASE_TRINKETS.slots[19].set_name("belt")
BASE_TRINKETS.slots[19].add_tag(tags.TRINKETS_BELT)
BASE_TRINKETS.slots[20].set_name("left_ankle")
BASE_TRINKETS.slots[20].add_tag(tags.TRINKETS_ANKLE)
BASE_TRINKETS.slots[21].set_name("right_Ankle")
BASE_TRINKETS.slots[21].add_tag(tags.TRINKETS_ANKLE)


BASE_EQUIPPMENT.slots[0].set_name("head")
BASE_EQUIPPMENT.slots[0].add_tag(tags.ARMOR_HEAD)
BASE_EQUIPPMENT.slots[1].set_name("body")
BASE_EQUIPPMENT.slots[1].add_tag(tags.ARMOR_BODY)
BASE_EQUIPPMENT.slots[2].set_name("hands")
BASE_EQUIPPMENT.slots[2].add_tag(tags.ARMOR_HANDS)
BASE_EQUIPPMENT.slots[3].set_name("legs")
BASE_EQUIPPMENT.slots[3].add_tag(tags.ARMOR_LEGS)
BASE_EQUIPPMENT.slots[4].set_name("feet")
BASE_EQUIPPMENT.slots[4].add_tag(tags.ARMOR_FEET)


BASE_USABLE.slots[0].set_name("right_shoulder")
BASE_USABLE.slots[0].add_tag(tags.HEAVY, tags.MASSIVE)
BASE_USABLE.slots[1].set_name("left_shoulder")
BASE_USABLE.slots[1].add_tag(tags.HEAVY, tags.MASSIVE)
BASE_USABLE.slots[2].set_name("right_hip")
BASE_USABLE.slots[2].add_tag(tags.MEDIUM, tags.LIGHT)
BASE_USABLE.slots[3].set_name("left_hip")
BASE_USABLE.slots[3].add_tag(tags.MEDIUM, tags.LIGHT)
BASE_USABLE.slots[4].set_name("right_thigh")
BASE_USABLE.slots[4].add_tag(tags.LIGHT)
BASE_USABLE.slots[5].set_name("left_thigh")
BASE_USABLE.slots[5].add_tag(tags.LIGHT)



BASE_ACTIVE.slots[0].set_name("right_hand")
BASE_ACTIVE.slots[0].add_tag(tags.USABLE)
BASE_ACTIVE.slots[1].set_name("left_hand")
BASE_ACTIVE.slots[1].add_tag(tags.USABLE)




HUMAN = [BASE_STASH.copy("STASH"), BASE_EQUIPPMENT.copy("EQUIPPMENT"), BASE_TRINKETS.copy("TRINKETS"), BASE_USABLE.copy("USABLE"), BASE_ACTIVE.copy("ACTIVE")]
ELF = [BASE_STASH.copy("STASH"), BASE_EQUIPPMENT.copy("EQUIPPMENT"), BASE_TRINKETS.copy("TRINKETS"), BASE_USABLE.copy("USABLE"), BASE_ACTIVE.copy("ACTIVE")]
DWARF = [BASE_STASH.copy("STASH"), BASE_EQUIPPMENT.copy("EQUIPPMENT"), BASE_TRINKETS.copy("TRINKETS"), BASE_USABLE.copy("USABLE"), BASE_ACTIVE.copy("ACTIVE")]
ORC = [BASE_STASH.copy("STASH"), BASE_EQUIPPMENT.copy("EQUIPPMENT"), BASE_TRINKETS.copy("TRINKETS"), BASE_USABLE.copy("USABLE"), BASE_ACTIVE.copy("ACTIVE")]
KITSUNE = [BASE_STASH.copy("STASH"), BASE_EQUIPPMENT.copy("EQUIPPMENT"), BASE_TRINKETS.copy("TRINKETS"), BASE_USABLE.copy("USABLE"), BASE_ACTIVE.copy("ACTIVE")]
KOBOLD = [BASE_STASH.copy("STASH"), BASE_EQUIPPMENT.copy("EQUIPPMENT"), BASE_TRINKETS.copy("TRINKETS"), BASE_USABLE.copy("USABLE"), BASE_ACTIVE.copy("ACTIVE")]




for i in [HUMAN, ELF, DWARF, ORC]:
  i[3].add_slot(6)
  i[3].slots[6].set_name("lower_back")
  i[3].slots[6].add_tag(tags.RANGED)


start = 22
tails = 9


for i in range(tails):
  KITSUNE[2].add_slot(start+i)
  KITSUNE[2].slots[start+i].set_name(f"tail_{i+1}")
  KITSUNE[2].slots[start+i].add_tag(tags.TRINKETS_TAIL)


KOBOLD[2].add_slot(22)
KOBOLD[2].slots[22].set_name(f"tail")
KOBOLD[2].slots[22].add_tag(tags.TRINKETS_TAIL)