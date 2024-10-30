from LocalLibrary import *
from commonLib import UUID
from main import Character





class Item:
    def __init__(self, name:str, id:int, description:str):
        self.name = name
        self.id = id
        self.description = description
    
    def register(self, name:str, id:int, description:str):
        self.name = name
        self.id = id
        self.description = description

    
    class Armor():
        '''
        All clothing items that provide some protect or special effect
        '''
        # def __init_subclass__(cls, slash_rating:int, peirce_rating:int, weight:int, body_location:str):
        #     super.__init__()
        #     body_locations = ["feet", "legs", "body", "head", "hands"]
        #     if body_location not in body_locations:
        #         raise ValueError(f"Invalid body location: \"{body_location}\". Must be one of \"{body_locations}\".")
        #     cls.slash_rating = slash_rating
        #     cls.peirce_rating = peirce_rating
        #     cls.weight = weight
        #     cls.body_location = body_location

        def __init_subclass__(cls):
            cls.items = []


        def register(cls, slash_rating:int, peirce_rating:int, weight:int, body_location:str):
            super.__init__()
            body_locations = ["feet", "legs", "body", "head", "hands"]
            if body_location not in body_locations:
                raise ValueError(f"Invalid body location: \"{body_location}\". Must be one of \"{body_locations}\".")
            cls.slash_rating = slash_rating
            cls.peirce_rating = peirce_rating
            cls.weight = weight
            cls.body_location = body_location


    class Clothes:
        '''
        All clothing wore entirely for athstetic
        '''
        def __init__(self):
            pass
          
          
    class Trinkets:
        '''
        Small wearable items such as necklaces, or ring
        '''
        def __init__(self):
            self.right_glove = None
            self.left_glove = None
            self.right_wrist = None
            self.left_wrist = None
            self.right_ankle = None
            self.left_ankle = None
            self.right_biscep = None
            self.left_biscep = None
            self.right_thigh = None
            self.left_thigh = None
            self.right_ear = None
            self.left_ear = None
            self.eyes = None
            self.neck = None

          
    class Weapons:
        '''
        Items that have offensive value 
        '''
        def __init__(self):
            pass


    class Tools:
        '''
        Items that have a special use, such a picks, and rope.
        '''
        def __init__(self):
            pass
        
        
    def __init__(self):
        self.general = list[Item]()
    
   
    class Money:
        def __init__(self):
            pass
          
   
    class QuestItems:
        def __init__(self):
            pass
          

    class General:
                def __init__(self):
                    pass




class Action:
    def __init__(self, action_type:str, cost:int):
        section_types = ["spell", "attack"]
        if action_type not in section_types:
            raise TypeError(f"{action_type} is not a valid action type.")
        
        self.cost = cost
        



class Effects:
    def __init__(self):
        self.instant_effects = list['InstantEffect']()
        self.temporary_effects = list['TemporaryEffect']()
        self.permanant_effects = list['PermanantEffect']()


    def Register_Instant_Effect(self, uuid:UUID):
        self.instant_effects.append(InstantEffect(uuid))

    def Register_Temporary_Effect(self, uuid:UUID):
        self.temporary_effects.append(InstantEffect(uuid))

    def Register_Permanant_Effect(self, uuid:UUID):
        self.permanant_effects.append(InstantEffect(uuid))

    def __str__(self):
        rows = ""
        i = len(self.instant_effects)
        t = len(self.temporary_effects)
        p = len(self.permanant_effects)
        while i > 0 or t > 0 or p > 0:
            temp = ""
            if i > 0:
                temp += f"{self.instant_effects[i-1].__format__("name")}".ljust(20)
            else:
                temp += "                    "
            temp += "|"
            if t > 0:
                temp += f"{self.temporary_effects[t-1].__format__("name")}".ljust(20)
            else:
                temp += "                    "
            temp += "|"
            if p > 0:
                temp += f"{self.permanant_effects[p-1].__format__("name")}".ljust(20)
            else:
                temp += "                    "
            temp += "\n"
            
            i -= 1
            t -= 1
            p -= 1
            rows += temp

        return f"Effect:\n"\
               f"                    |                    |                    \n"\
               f"{rows}"\
               f"                    |                    |                    "


class EffectCategory:
    def __init__(self, uuid:UUID, name:str="N/A"):
        self.__uuid = uuid
        self.name = name
        self.effects = list[Effect]()
    
    @property
    def uuid(self):
        return self.__uuid


    def change_uuid(self, uuid:UUID):
        answer = input("Changeing the UUID of a EffectCatagory may cause fatal errors, are you sure you want to continue? (y/n): ")
        while True:
          if answer == "y":
              self.__uuid = uuid
              break
          elif answer == "n":
              break
          else:
              print("invalid answer please answer with \'y\' or \'n\'")


    def add_effect(self, effect:"Effect"):
        self.effects.append(effect)


    def __str__(self) -> str:
        return self.uuid


class Effect:
    '''
This is a parent class and should not be used directly
    '''
    def __init__(self, uuid:UUID):
        self.__uuid = uuid
        self.name = "N/A"
        self.description = "N/A"
        self.methods = list[tuple[str, str, int]]()
        self.catagory = list[str]()
        
        self.max_health = 0
        self.max_stamina = 0
        self.max_mana = 0
        self.health = 0
        self.stamina = 0
        self.mana = 0
        self.strength = 0
        self.constitution = 0
        self.agility = 0
        self.wisdom = 0
        self.intelligence = 0
        self.charisma = 0
    
    @property
    def uuid(self) -> UUID:
        return self.__uuid
    

    def add_name(self, name:str):
        self.name = name
    
    
    def add_description(self, description:str):
        self.description = description
    

    def add_catagory(self, category:EffectCategory):
        getattr(category, "add_effect")(self)

    
    def add_effect(self, *args):
        '''
Adds a new effect to the Effect based on the args given.
the first argument is the function, everything after is passed into the function

Current options for instant effects:
  damage(stat_to_damage, amount_of_damage)
  heal(stat_to_heal, amount_of_heal)

Current options for temporary effects:
  poison(stat_to_damage, amount_of_damage)
  weaken(stat_to_weaken, amount_to_weaken
  regen(stat_to_heal, amount_of_heal_per_second)
  boost(stat_to_boost, amount_to_boost)

Current options for permanent effects:
  cripple(stat_to_weaken, amount_to_weaken)
  boost(stat_to_boost, amount_of_boost)
  lycanthopey()
'''
        self.methods.append(args)
    
    def remove_effect(self, *args):
        '''
removes an added effect, you must put in the exact args in the exact order they were added in for it to work
        '''
        try:
          self.methods.remove(args)
        except ValueError as e:
            if str(e) == "list.remove(x): x not in list":
                raise ValueError(f"{args} is not an added effect")
            else:
                raise ValueError(e)
            
    
    # def apply_effet(self, target: "Character"):
        # target.status.
            


class InstantEffect(Effect):
    def __init__(self, uuid:UUID):
        super().__init__(uuid)
        self.__uuid = uuid
    

    def __str__(self) -> str:
        methods = ""
        for method in self.methods:
            methods += f"{method[0]}, "
        methods = methods.removesuffix(", ")
        return f"UUID: {self.__uuid}"\
f"{ f"\nName: {self.name}" if self.name != "" else ""}"\
f"{ f"\nDescription: {self.description}" if self.description != "" else ""}"\
f"{ f"\nEffects: {methods}" if methods  != [] else ""}"\
f"{ f"\nCatagories: {self.catagory}" if self.catagory  != [] else ""}"
    

    def __format__(self, format_spec):
        '''
        Options:\n
            \"effects\": returns a string of the effects\n
            \"catagories\": returns a string of the catagories\n
            \"description\": returns a string of the description\n
            \"name\": returns a string of the name\n
            \"uuid\": returns a string of the uuid
        '''
        if format_spec == "effects":
            return ", ".join(self.methods)
        elif format_spec == "catagories":
            return ", ".join(self.catagory)
        elif format_spec == "description":
            return self.description
        elif format_spec == "name":
            return self.name
        elif format_spec == "uuid":
            return self.uuid


    def damage(self, var_tuple:tuple[str, str, int]):
        '''
        this function should not be called directly, instead use the add_effect method

        args = stat_to_damage, amount_to_damage

        effectable stats: "health", "stamina", "mana"
        '''
        damage_type:str = var_tuple[1]
        amount:int = var_tuple[2]
        if amount < 1:
            raise ValueError("Instant Damage must be greater than zero.")
        damageable = ["health", "stamina", "mana"]
        if damage_type not in damageable:
          raise ValueError(f"{damage_type}, is not damageable stat, pick from: {damageable}")
        
        self.__setattr__(damage_type, self.__getattribute__(damage_type) - amount)


    def heal(self, var_tuple:tuple[str, str, int]):
        '''
        this function should not be called directly, instead use the add_effect method

        args = stat_to_heal, amount_to_heal

        effectable stats: "health", "stamina", "mana"
        '''
        heal_type:str = var_tuple[1]
        amount:int = var_tuple[2]
        if amount < 1:
            raise ValueError("Instant Heal must be greater than zero.")
        healable = ["health", "stamina", "mana"]
        if heal_type not in ["health", "stamina", "mana"]:
          raise ValueError(f"{heal_type}, is not healable stat, pick from: {healable}")

        self.__setattr__(heal_type, self.__getattribute__(heal_type) + amount)


    def trigger(self):
        for method in self.methods:
          self.__getattribute__(method[0])(method)


class TemporaryEffect(Effect):
    def __init__(self, name:str):
        super().__init__(name)
        self.duration = 0.0
        self.time_passed = .0


    def __str__(self) -> str:
        methods = ""
        for method in self.methods:
            methods += f"{method[0]}, "
        methods = methods.removesuffix(", ")
        return f"UUID: {self.__uuid}"\
f"{ f"\nName: {self.name}" if self.name != "" else ""}"\
f"{ f"\nDescription: {self.description}" if self.description != "" else ""}"\
f"{ f"\nEffects: {methods}" if methods  != [] else ""}"\
f"{ f"\nCatagories: {self.catagory}" if self.catagory  != [] else ""}"


    def poison(self, var_tuple:tuple[str, str, int]):
        '''
        this function should not be called directly, instead use the add_effect method

        args = stat_to_poisen, amount_of_damage_per_second

        damageable_stats: "health", "stamina", "mana"
        '''
        damage_type:str = var_tuple[1]
        amount:int = var_tuple[2]
        if amount < 1:
            raise ValueError("Amount of damage must be greater than 0.")
        damageable = ["health", "stamina", "mana"]
        if damage_type not in damageable:
          raise ValueError(f"{damage_type}, is not damageable stat, pick from: {damageable}")
        
        self.__setattr__(damage_type, self.__getattribute__(damage_type) - (amount*self.time_passed))
    

    def weaken(self, var_tuple:tuple[str, str, int]):
        '''
        this function should not be called directly, instead use the add_effect method

        args = stat_to_weaken, amount_to_weaken

        effectable stats: "max_health", "max_stamina", "max_mana", "strength", "constitution", "agility", "wisdom", "intelligence", "charisma"
        '''
        damage_type:str = var_tuple[1]
        amount:int = var_tuple[2]
        if amount < 1:
            raise ValueError("Amount of damage must be greater than 0.")
        damageable = ["max_health", "max_stamina", "max_mana", "strength", "constitution", "agility", "wisdom", "intelligence", "charisma"]
        if damage_type not in damageable:
          raise ValueError(f"{damage_type}, is not a stat")
        
        if self.duration > 0:
            self.__setattr__(damage_type, -amount)
        else:
            self.__setattr__(damage_type, self.__getattribute__(damage_type) + amount)


    def regen(self, var_tuple:tuple[str, str, int]):
        '''
        this function should not be called directly, instead use the add_effect method

        args = stat_to_heal, amount_of_heal_per_second

        damageable_stats: "health", "stamina", "mana"
        '''
        heal_type:str = var_tuple[1]
        amount:int = var_tuple[2]
        healable = ["health", "stamina", "mana"]
        if heal_type not in healable:
          raise ValueError(f"{heal_type}, is not healable stat, pick from: {healable}")

        self.__setattr__(heal_type, self.__getattribute__(heal_type) + (amount*self.time_passed))
        

    def boost(self, var_tuple:tuple[str, str, int]):
        '''
        this function should not be called directly, instead use the add_effect method

        args = stat_to_boost, amount_of_boost

        damageable_stats: "max_health", "max_stamina", "max_mana", "strength", "constitution", "agility", "wisdom", "intelligence", "charisma"
        '''
        heal_type:str = var_tuple[1]
        amount:int = var_tuple[2]
        healable = ["max_health", "max_stamina", "max_mana", "strength", "constitution", "agility", "wisdom", "intelligence", "charisma"]
        if heal_type not in healable:
          raise ValueError(f"{heal_type}, is not healable stat, pick from: {healable}")
        if amount < 1:
            raise ValueError("Temporary Boost requires a positive number")
        
        if self.duration > 0:
            self.__setattr__(heal_type, amount)
        else:
            self.__setattr__(heal_type, self.__getattribute__(heal_type) - amount)
    

    def trigger(self, duration:float):
        self.duration = duration
        for method in self.methods:
          self.__getattribute__(method[0])(method)
    

    def triggered(self, time_passed:float):
        self.duration -= time_passed
        self.time_passed = time_passed


class PermanantEffect(Effect):
    def __init__(self, name:str):
        super().__init__(name)
        self.end = False


    def __str__(self):
        methods = ""
        for method in self.methods:
            methods += f"{method[0]}, "
        methods = methods.removesuffix(", ")
        return f"UUID: {self.__uuid}"\
f"{ f"\nName: {self.name}" if self.name != "" else ""}"\
f"{ f"\nDescription: {self.description}" if self.description != "" else ""}"\
f"{ f"\nEffects: {methods}" if methods  != [] else ""}"\
f"{ f"\nCatagories: {self.catagory}" if self.catagory  != [] else ""}"
    

    def weaken(self, var_tuple:tuple[str, str, int]):
        '''
        this function should not be called directly, instead use the add_effect method

        args = stat_to_weaken, amount_to_weaken

        effectable stats: "max_health", "max_stamina", "max_mana", "strength", "constitution", "agility", "wisdom", "intelligence", "charisma"
        '''
        damage_type:str = var_tuple[1]
        amount:int = var_tuple[2]
        if amount < 1:
            raise ValueError("Amount of damage must be greater than 0.")
        damageable = ["max_health", "max_stamina", "max_mana", "strength", "constitution", "agility", "wisdom", "intelligence", "charisma"]
        if damage_type not in damageable:
          raise ValueError(f"{damage_type}, is not a stat")
        
        self.__setattr__(damage_type, -amount)
        if self.end:
          self.__setattr__(damage_type, self.__getattribute__(damage_type) + amount)
            


    def boost(self, var_tuple:tuple[str, str, int]):
        '''
        this function should not be called directly, instead use the add_effect method

        args = stat_to_boost, amount_of_boost

        damageable_stats: "max_health", "max_stamina", "max_mana", "strength", "constitution", "agility", "wisdom", "intelligence", "charisma"
        '''
        heal_type:str = var_tuple[1]
        amount:int = var_tuple[2]
        healable = ["max_health", "max_stamina", "max_mana", "strength", "constitution", "agility", "wisdom", "intelligence", "charisma"]
        if heal_type not in healable:
          raise ValueError(f"{heal_type}, is not healable stat, pick from: {healable}")
        if amount < 1:
            raise ValueError("Temporary Boost requires a positive number")
        
        self.__setattr__(heal_type, amount)
        if self.end:
          self.__setattr__(heal_type, self.__getattribute__(heal_type) + amount)
    

    def lycanthopey(self):
        '''
        this function should not be called directly, instead use the add_effect method

        no args
        '''
        self.wereworlf = True
            
    

    def trigger(self):
        for method in self.methods:
          self.__getattribute__(method[0])(method)







# damage = InstantEffect(UUID("46854bc4-93e8-8cf5-370b-5ddb36597118"))
# category = EffectCategory(UUID(), "Test Category")



# damage.add_name("Test Effect")
# damage.add_description("Just an effect to test out stuff")
# damage.add_catagory(category)
# damage.add_effect("damage", "health", 2)
# damage.add_effect("damage", "health", 2)
# # damage.remove_effect("damage", "health", 2)
# # damage.trigger()

# print(f"Damage:\n{damage}")

effects = Effects()
print(effects)
effects.Register_Instant_Effect(UUID())
effects.Register_Instant_Effect(UUID())
effects.Register_Instant_Effect(UUID())
effects.instant_effects[0].add_name("name test")
effects.instant_effects[1].add_name("name test1")
effects.instant_effects[2].add_name("name test2")
print(effects)