from registers import BodyPart, GripperPart



ARMOR_HEAD = BodyPart().set_name("Armor Slot Head").register("ARMOR_HEAD")
ARMOR_CHEST = BodyPart().set_name("Armor Slot Chest").register("ARMOR_CHEST")
ARMOR_LEGS = BodyPart().set_name("Armor Slot Legs").register("ARMOR_LEGS")
ARMOR_FEET = BodyPart().set_name("Armor Slot Feet").register("ARMOR_FEET")
ARMOR_HANDS = BodyPart().set_name("Armor Slot Hands").register("ARMOR_HANDS")

HEAD = BodyPart().set_name("Clothing Slot Head").register("HEAD")
CHEST = BodyPart().set_name("Clothing Slot Chest").register("CHEST")
HANDS = BodyPart().set_name("Clothing Slot Hands").register("HANDS")
LEGS = BodyPart().set_name("Clothing Slot Legs").register("LEGS")
FEET = BodyPart().set_name("Clothing Slot Feet").register("FEET")
BACK = BodyPart().set_name("Clothing Slot Back").register("BACK")
UPPER_UNDIES = BodyPart().set_name("Clothing Slot Upper Undies").register("UPPER_UNDIES")
LOWER_UNDIES = BodyPart().set_name("Clothing Slot Lower Undies").register("LOWER_UNDIES")
FEET_UNDIES = BodyPart().set_name("Clothing Slot Feet Undies").register("FEET_UNDIES")

WRIST_1 = BodyPart().set_name("Right Wrist").register("WRIST_1")
WRIST_2 = BodyPart().set_name("Left Wrist").register("WRIST_2")
FACE = BodyPart().set_name("Face").register("FACE")
NECK_1 = BodyPart().set_name("Neck").register("NECK_1")
EAR_1 = BodyPart().set_name("Right Ear").register("EAR_1")
EAR_2 = BodyPart().set_name("Left Ear").register("EAR_2")

hands = ["Right Hand", "Left Hand"]
fingers = ["Thumb", "Index Finger", "Middle Finger", "Ring Finger", "Pinky Finger"]

for x in range(2):
  for y in range(5):
    BodyPart().set_name(f"{hands[x]}-{fingers[y]}").register(f"FINGER{x}_{y}")

WEAPON_RIGHT_SHOULDER = BodyPart().set_name("Right Shoulder Holseter").register("WEAPON_RIGHT_SHOULDER")
WEAPON_LEFT_SHOULDER = BodyPart().set_name("Left Shoulder").register("WEAPON_LEFT_SHOULDER")
WEAPON_RIGHT_HIP = BodyPart().set_name("Right Hip Holster").register("WEAPON_RIGHT_HIP")
WEAPON_LEFT_HIP = BodyPart().set_name("Left Hip Holster").register("WEAPON_LEFT_HIP")
WEAPON_RIGHT_THIGH = BodyPart().set_name("Right Thigh Holster").register("WEAPON_RIGHT_THIGH")
LEFT_THIGH = BodyPart().set_name("Left Thigh Holster").register("LEFT_THIGH")



HAND_1 = GripperPart().set_name("Right Hand").register("HAND_1")
HAND_2 = GripperPart().set_name("Left Hand").register("HAND_2")