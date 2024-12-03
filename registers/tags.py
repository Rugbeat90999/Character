from define import Tag




ITEM = Tag("item")



WEARABLE = Tag("wearable", ITEM)
USABLE = Tag("usable", ITEM)



ARMOR = Tag("armor", WEARABLE)
CLOTHES = Tag("cloths", WEARABLE)
TRINKETS = Tag("trinkets", WEARABLE)


WEAPON = Tag("weapon", USABLE)
TOOL = Tag("tool", USABLE)



ARMOR_HEAD = Tag("head", ARMOR)
ARMOR_BODY = Tag("body", ARMOR)
ARMOR_HANDS = Tag("hands", ARMOR)
ARMOR_TAIL = Tag("tail", ARMOR)
ARMOR_LEGS = Tag("legs", ARMOR)
ARMOR_FEET = Tag("feet", ARMOR)

CLOTHES_HEAD = Tag("head", CLOTHES)
CLOTHES_UPPPER_UNDIES = Tag("upperundies", CLOTHES)
CLOTHES_BODY = Tag("body", CLOTHES)
CLOTHES_HANDS = Tag("hands", CLOTHES)
CLOTHES_TAILS = Tag("tails", CLOTHES)
CLOTHES_UNDERWEAR = Tag("lowerundies", CLOTHES)
CLOTHES_LEGS = Tag("legs", CLOTHES)
CLOTHES_SOCKS = Tag("feetundies", CLOTHES)
CLOTHES_FEET = Tag("feet", CLOTHES)

TRINKETS_FACE = Tag("face", TRINKETS)
TRINKETS_EAR = Tag("ear", TRINKETS)
TRINKETS_NECK = Tag("neck", TRINKETS)
TRINKETS_CAPE = Tag("cape", TRINKETS)
TRINKETS_WRIST = Tag("wrist", TRINKETS)
TRINKETS_HAND = Tag("hand", TRINKETS)
TRINKETS_FINGER = Tag("finger", TRINKETS)
TRINKETS_TAIL = Tag("tail", TRINKETS)
TRINKETS_BELT = Tag("belt", TRINKETS)
TRINKETS_ANKLE = Tag("ankle", TRINKETS)


MASSIVE = Tag("massive", WEAPON)
HEAVY = Tag("heavy", WEAPON)
MEDIUM = Tag("medium", WEAPON)
LIGHT = Tag("light", WEAPON)
RANGED = Tag("bow", WEAPON)

SILVER = Tag("silver", WEAPON)