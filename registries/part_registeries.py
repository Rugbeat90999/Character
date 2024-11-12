from registers import BodyPart, Gripper
from registries.registry_registeries import *


ARMOR_HEAD = BodyPart().set_name("Armor Slot Head").register("ARMOR_HEAD", A_PARTS)
ARMOR_CHEST = BodyPart().set_name("Armor Slot Chest").register("ARMOR_CHEST", A_PARTS)
ARMOR_LEGS = BodyPart().set_name("Armor Slot Legs").register("ARMOR_LEGS", A_PARTS)
ARMOR_FEET = BodyPart().set_name("Armor Slot Feet").register("ARMOR_FEET", A_PARTS)
ARMOR_HANDS = BodyPart().set_name("Armor Slot Hands").register("ARMOR_HANDS", A_PARTS)

HEAD = BodyPart().set_name("Clothing Slot Head").register("HEAD", A_PARTS)
CHEST = BodyPart().set_name("Clothing Slot Chest").register("CHEST", A_PARTS)
HANDS = BodyPart().set_name("Clothing Slot Hands").register("HANDS", A_PARTS)
LEGS = BodyPart().set_name("Clothing Slot Legs").register("LEGS", A_PARTS)
FEET = BodyPart().set_name("Clothing Slot Feet").register("FEET", A_PARTS)
BACK = BodyPart().set_name("Clothing Slot Back").register("BACK", A_PARTS)
UPPER_UNDIES = BodyPart().set_name("Clothing Slot Upper Undies").register("UPPER_UNDIES", A_PARTS)
LOWER_UNDIES = BodyPart().set_name("Clothing Slot Lower Undies").register("LOWER_UNDIES", A_PARTS)
FEET_UNDIES = BodyPart().set_name("Clothing Slot Feet Undies").register("FEET_UNDIES", A_PARTS)

WRIST_1 = BodyPart().set_name("Right Wrist").register("WRIST_1", A_PARTS)
WRIST_2 = BodyPart().set_name("Left Wrist").register("WRIST_2", A_PARTS)
FACE = BodyPart().set_name("Face").register("FACE", A_PARTS)
NECK_1 = BodyPart().set_name("Neck").register("NECK_1", A_PARTS)
EAR_1 = BodyPart().set_name("Right Ear").register("EAR_1", A_PARTS)
EAR_2 = BodyPart().set_name("Left Ear").register("EAR_2", A_PARTS)

hands = ["Right Hand", "Left Hand"]
fingers = ["Thumb", "Index Finger", "Middle Finger", "Ring Finger", "Pinky Finger"]

for x in range(2):
  for y in range(5):
    BodyPart().set_name(f"{hands[x]}-{fingers[y]}").register(f"FINGER{x}_{y}", A_PARTS)

WEAPON_RIGHT_SHOULDER = BodyPart().set_name("Right Shoulder Holseter").register("WEAPON_RIGHT_SHOULDER", A_PARTS)
WEAPON_LEFT_SHOULDER = BodyPart().set_name("Left Shoulder").register("WEAPON_LEFT_SHOULDER", A_PARTS)
WEAPON_RIGHT_HIP = BodyPart().set_name("Right Hip Holster").register("WEAPON_RIGHT_HIP", A_PARTS)
WEAPON_LEFT_HIP = BodyPart().set_name("Left Hip Holster").register("WEAPON_LEFT_HIP", A_PARTS)
WEAPON_RIGHT_THIGH = BodyPart().set_name("Right Thigh Holster").register("WEAPON_RIGHT_THIGH", A_PARTS)
LEFT_THIGH = BodyPart().set_name("Left Thigh Holster").register("LEFT_THIGH", A_PARTS)



HAND_1 = Gripper().set_name("Right Hand").register("HAND_1", A_PARTS)
HAND_2 = Gripper().set_name("Left Hand").register("HAND_2", A_PARTS)

for x in range(9):
  Gripper().set_name(f"Tail {x+1}").register(f"TAIL_{x+1}", A_PARTS)