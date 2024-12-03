from registers import *
from define import Character
from CommonLib.classes import Path

class Race:
  def __init__(self, race: str):
    self.inventories = []
    self.effects = []

    match race:
      case "human":
        self.inventories.append(inventories.HUMAN)
      case "elf":
        self.inventories.append(inventories.ELF)
      case "dwarf":
        self.inventories.append(inventories.DWARF)
      case "orc":
        self.inventories.append(inventories.ORC)
      case "kitsune":
        self.inventories.append(inventories.KITSUNE)
      case "kobold":
        self.inventories.append(inventories.KOBOLD)
      case "tiny":
        # TODO: add tiny race (5 inch tall human)
        raise NotImplementedError("race \"pixie\" is not yet implemented.")
      case "giant":
        # TODO: add tiny race (5 inch tall human)
        raise NotImplementedError("race \"pixie\" is not yet implemented.")
      case "pixie":
        # TODO: add pixie race
        raise NotImplementedError("race \"pixie\" is not yet implemented.")
      case "fairy":
        # TODO: add fairy race
        raise NotImplementedError("race \"fairy\" is not yet implemented.")
      case "sprite":
        # TODO: add sprite race
        raise NotImplementedError("race \"sprite\" is not yet implemented.")
      case "imp":
        # TODO: add imp race
        raise NotImplementedError("race \"imp\" is not yet implemented.")
      case "gnome":
        # TODO: add gnome race
        raise NotImplementedError("race \"gnome\" is not yet implemented.")
      case "goblin":
        # TODO: add goblin race
        raise NotImplementedError("race \"goblin\" is not yet implemented.")
      case "hobgoblin":
        # TODO: add hobgoblin race
        raise NotImplementedError("race \"hobgoblin\" is not yet implemented.")
      case "leprechaun":
        # TODO: add leprechaun race
        raise NotImplementedError("race \"leprechaun\" is not yet implemented.")
      case "troll":
        # TODO: add troll race
        raise NotImplementedError("race \"troll\" is not yet implemented.")
      case _:
        raise ValueError(f"Invalid race: {race}")






# ME_PATH = Path("./char_data/me.char")
# ME = Character(ME_PATH, "ME")

print(items.AMULET_OF_FORTUNE)