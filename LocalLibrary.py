from CommonLib.classes import UUID




class MoneyError(BaseException):
    def __init__(self, message):
        print(f"Money Error: {message}")




class BodyLocation:
    HEAD = B"Head"
    CHEST = B"Chest"
    HANDS = B"Hands"
    LEGS = B"Legs"
    FEET = B"Feet"

    WRIST1 = B"Wrist1"
    WRIST2 = B"Wrist1"

    FACE = B"Face"

    NECK1 = B"Neck1"
    NECK2 = B"Neck2"

    EAR1 = B"Ear1"
    EAR2 = B"Ear2"

    FINGER1 = B"Finger1"
    FINGER2 = B"Finger2"
    FINGER3 = B"Finger3"
    FINGER4 = B"Finger4"
    FINGER5 = B"Finger5"
    FINGER6 = B"Finger6"
    FINGER7 = B"Finger7"
    FINGER8 = B"Finger8"
    FINGER9 = B"Finger9"
    FINGER10 = B"Finger10"




def UUID_search(uuid:UUID, search_list:list):
    for index in range(len(search_list)):
        if uuid == search_list[index].uuid:
            return index
    return -1
    