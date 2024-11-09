from registers import BodyPart, Griper, BodyLocations, ItemLocations




BodyPart().set_name("Armor Slot Head").register("ARMOR_HEAD")
BodyPart().set_name("Armor Slot Chest").register("ARMOR_CHEST")
BodyPart().set_name("Armor Slot Legs").register("ARMOR_LEGS")
BodyPart().set_name("Armor Slot Feet").register("ARMOR_FEET")
BodyPart().set_name("Armor Slot Hands").register("ARMOR_HANDS")

BodyPart().set_name("Clothing Slot Head").register("HEAD")
BodyPart().set_name("Clothing Slot Chest").register("CHEST")
BodyPart().set_name("Clothing Slot Hands").register("HANDS")
BodyPart().set_name("Clothing Slot Legs").register("LEGS")
BodyPart().set_name("Clothing Slot Feet").register("FEET")
BodyPart().set_name("Clothing Slot Back").register("BACK")
BodyPart().set_name("Clothing Slot Upper Undies").register("UPPER_UNDIES")
BodyPart().set_name("Clothing Slot Lower Undies").register("LOWER_UNDIES")
BodyPart().set_name("Clothing Slot Feet Undies").register("FEET_UNDIES")

BodyPart().set_name("Right Wrist").register("WRIST_1")
BodyPart().set_name("Left Wrist").register("WRIST_2")
BodyPart().set_name("Face").register("FACE")
BodyPart().set_name("Neck").register("NECK_1")
BodyPart().set_name("Right Ear").register("EAR_1")
BodyPart().set_name("Left Ear").register("EAR_2")

hands = ["Right Hand", "Left Hand"]
fingers = ["Thumb", "Index Finger", "Middle Finger", "Ring Finger", "Pinky Finger"]

for x in range(2):
  for y in range(5):
    BodyPart().set_name(f"{hands[x]}-{fingers[y]}").register(f"FINGER{x}_{y}")

BodyPart().set_name("Right Shoulder Holseter").register("WEAPON_RIGHT_SHOULDER")
BodyPart().set_name("left_shoulder").register("WEAPON_LEFT_SHOULDER")
BodyPart().set_name("Right Hip Holster").register("WEAPON_RIGHT_HIP")
BodyPart().set_name("Left Hip Holster").register("WEAPON_LEFT_HIP")
BodyPart().set_name("Right Thigh Holster").register("WEAPON_RIGHT_THIGH")
BodyPart().set_name("Left Thigh Holster").register("LEFT_THIGH")



# Griper().set_name("Right Hand").register("HAND_1")
# Griper().set_name("Left Hand").register("HAND_2")


# ItemLocations.unregister(ItemLocations.HAND_1)