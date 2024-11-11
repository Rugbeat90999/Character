from registers import BodyPart, Gripper
from registries.registry_registeries import *


ARMOR_HEAD = BodyPart().set_name("Armor Slot Head").register("ARMOR_HEAD", PARTS)
ARMOR_CHEST = BodyPart().set_name("Armor Slot Chest").register("ARMOR_CHEST", PARTS)
ARMOR_LEGS = BodyPart().set_name("Armor Slot Legs").register("ARMOR_LEGS", PARTS)
ARMOR_FEET = BodyPart().set_name("Armor Slot Feet").register("ARMOR_FEET", PARTS)
ARMOR_HANDS = BodyPart().set_name("Armor Slot Hands").register("ARMOR_HANDS", PARTS)

HEAD = BodyPart().set_name("Clothing Slot Head").register("HEAD", PARTS)
CHEST = BodyPart().set_name("Clothing Slot Chest").register("CHEST", PARTS)
HANDS = BodyPart().set_name("Clothing Slot Hands").register("HANDS", PARTS)
LEGS = BodyPart().set_name("Clothing Slot Legs").register("LEGS", PARTS)
FEET = BodyPart().set_name("Clothing Slot Feet").register("FEET", PARTS)
BACK = BodyPart().set_name("Clothing Slot Back").register("BACK", PARTS)
UPPER_UNDIES = BodyPart().set_name("Clothing Slot Upper Undies").register("UPPER_UNDIES", PARTS)
LOWER_UNDIES = BodyPart().set_name("Clothing Slot Lower Undies").register("LOWER_UNDIES", PARTS)
FEET_UNDIES = BodyPart().set_name("Clothing Slot Feet Undies").register("FEET_UNDIES", PARTS)

WRIST_1 = BodyPart().set_name("Right Wrist").register("WRIST_1", PARTS)
WRIST_2 = BodyPart().set_name("Left Wrist").register("WRIST_2", PARTS)
FACE = BodyPart().set_name("Face").register("FACE", PARTS)
NECK_1 = BodyPart().set_name("Neck").register("NECK_1", PARTS)
EAR_1 = BodyPart().set_name("Right Ear").register("EAR_1", PARTS)
EAR_2 = BodyPart().set_name("Left Ear").register("EAR_2", PARTS)

hands = ["Right Hand", "Left Hand"]
fingers = ["Thumb", "Index Finger", "Middle Finger", "Ring Finger", "Pinky Finger"]

for x in range(2):
  for y in range(5):
    BodyPart().set_name(f"{hands[x]}-{fingers[y]}").register(f"FINGER{x}_{y}", PARTS)

WEAPON_RIGHT_SHOULDER = BodyPart().set_name("Right Shoulder Holseter").register("WEAPON_RIGHT_SHOULDER", PARTS)
WEAPON_LEFT_SHOULDER = BodyPart().set_name("Left Shoulder").register("WEAPON_LEFT_SHOULDER", PARTS)
WEAPON_RIGHT_HIP = BodyPart().set_name("Right Hip Holster").register("WEAPON_RIGHT_HIP", PARTS)
WEAPON_LEFT_HIP = BodyPart().set_name("Left Hip Holster").register("WEAPON_LEFT_HIP", PARTS)
WEAPON_RIGHT_THIGH = BodyPart().set_name("Right Thigh Holster").register("WEAPON_RIGHT_THIGH", PARTS)
LEFT_THIGH = BodyPart().set_name("Left Thigh Holster").register("LEFT_THIGH", PARTS)



HAND_1 = Gripper().set_name("Right Hand").register("HAND_1", PARTS)
HAND_2 = Gripper().set_name("Left Hand").register("HAND_2", PARTS)

for x in range(9):
  Gripper().set_name(f"Tail {x+1}").register(f"TAIL_{x+1}", PARTS)