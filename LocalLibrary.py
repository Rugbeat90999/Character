from commonLib import UUID

class MoneyError(BaseException):
    def __init__(self, message):
        print(f"Money Error: {message}")


def UUID_search(uuid:UUID, search_list:list):
    for index in range(len(search_list)):
        if uuid == search_list[index].uuid:
            return index
    return -1
    