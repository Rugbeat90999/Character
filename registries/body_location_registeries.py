from registers import BodyLocation

BodyLocation.register("ARMOR_HEAD")
BodyLocation.register("ARMOR_CHEST")
BodyLocation.register("ARMOR_LEGS")
BodyLocation.register("ARMOR_FEET")
BodyLocation.register("ARMOR_HANDS")

BodyLocation.register("HEAD")
BodyLocation.register("CHEST")
BodyLocation.register("HANDS")
BodyLocation.register("LEGS")
BodyLocation.register("FEET")
BodyLocation.register("BACK")
BodyLocation.register("UPPER_UNDIES")
BodyLocation.register("LOWER_UNDIES")
BodyLocation.register("FEET_UNDIES")

BodyLocation.register("WRIST_1")
BodyLocation.register("WRIST_2")
BodyLocation.register("FACE")
BodyLocation.register("NECK_1")
BodyLocation.register("NECK_2")
BodyLocation.register("EAR_1")
BodyLocation.register("EAR_2")

for x in range(2):
  for y in range(5):
    BodyLocation.register(f"FINGER{x}_{y}")

BodyLocation.register("WEAPON_RIGHT_SHOULDER")
BodyLocation.register("WEAPON_LEFT_SHOULDER")
BodyLocation.register("WEAPON_RIGHT_HIP")
BodyLocation.register("WEAPON_LEFT_HIP")
BodyLocation.register("WEAPON_RIGHT_THIGH")
BodyLocation.register("WEAPON_LEFT_THIGH")