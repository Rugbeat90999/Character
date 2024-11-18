from define import Tag

ITEM = Tag("item")



WEARABLE = Tag("wearable", ITEM)
USABLE = Tag("tool", ITEM)



ARMOR = Tag("armor", WEARABLE)
CLOTHES = Tag("cloths", WEARABLE)
TRINKETS = Tag("trinkets", WEARABLE)


WEAPON = Tag("weapon", USABLE)
TOOL = Tag("tool", USABLE)



ARMOR_HEAD = Tag("head", ARMOR)
ARMOR_BODY = Tag("body", ARMOR)
ARMOR_HANDS = Tag("hands", ARMOR)
ARMOR_LEGS = Tag("legs", ARMOR)
ARMOR_FEET = Tag("feet", ARMOR)

CLOTHES_HEAD = Tag("head", CLOTHES)
CLOTHES_UPPPER_UNDIES = Tag("upperundies", CLOTHES)
CLOTHES_BODY = Tag("body", CLOTHES)
CLOTHES_HANDS = Tag("hands", CLOTHES)
CLOTHES_UNDERWEAR = Tag("underwear", CLOTHES)
CLOTHES_LEGS = Tag("legs", CLOTHES)
CLOTHES_SOCKS = Tag("socks", CLOTHES)
CLOTHES_FEET = Tag("feet", CLOTHES)

TRINKETS_FACE = Tag("face", TRINKETS)
TRINKETS_NECK = Tag("neck", TRINKETS)
TRINKETS_CAPE = Tag("cape", TRINKETS)
TRINKETS_BELT = Tag("belt", TRINKETS)
TRINKETS_WRIST = Tag("wrist", TRINKETS)
TRINKETS_ANKLE = Tag("ankle", TRINKETS)
TRINKETS_EAR = Tag("ear", TRINKETS)