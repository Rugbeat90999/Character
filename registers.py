from LocalLibrary import *
from CommonLib.classes import UUID, NotUniqueUUIDError
from CommonLib.functional_classes import staticproperty, staticstr






class Items(metaclass=staticstr):
    '''
    All items that can be used or held by players
    '''
    def __str__():
        pass
    
    class Wearable(metaclass=staticstr):
        pass
    

    class Useable(metaclass=staticstr):
        pass


    class Other(metaclass=staticstr):
        pass
    



class Item:
    def __init__(self, uuid:UUID):
        self.__uuid = uuid
        self.__regitry_name = uuid.alphabetic_version
        self.name = "N/A"
        self.description = "N/A"
        self.value = 0
        self.weight = 0

    def __str__(self):
        # TODO: add this
        return "add this str"



class Armor(Item):
        '''
        Wearable items that provide protect
        '''

        def __init__(self, uuid:UUID):
            super().__init__(uuid)
            self.slash_rating = 0
            self.peirce_rating = 0
            self.weight = 0
            self.body_location = ""


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
        





class Effects(metaclass=staticstr):
    class Instant(metaclass=staticstr):
        all = list['InstantEffect']()
        registered = list[str]()

        
        def __str__() -> str:
            rows = ""
            for effect in Effects.Instant.all:
                rows += f"{effect}\n"
            rows = rows.removesuffix("\n")
            return f"Instant Effects:\n"\
                   f"{rows}"
        

        

        @staticmethod
        def register(effect:"InstantEffect", registrey_name:str):
            for registered_effect in Effects.Instant.all + Effects.Permanent.all + Effects.Temporary.all:
                registered_effect.uuid.compare(effect.uuid)

            Effects.Instant.all.append(effect)
            Effects.Instant.registered.append(effect.registry_name)
            setattr(Effects.Instant, registrey_name, effect)


    class Temporary(metaclass=staticstr):
        all = list['TemporaryEffect']()
        registered = list[str]()


        def __str__() -> str:
            rows = ""
            for effect in Effects.Instant.all:
                rows += f"{effect}\n"
            rows = rows.removesuffix("\n")
            return f"Temporary Effects:\n"\
                   f"{rows}"


        @staticmethod
        def register(effect:"TemporaryEffect", registrey_name:str):
            for registered_effect in Effects.Instant.all + Effects.Permanent.all + Effects.Temporary.all:
                registered_effect.uuid.compare(effect.uuid)
            Effects.Temporary.all.append(effect)
            Effects.Temporary.registered.append(effect.registry_name)
            setattr(Effects.Temporary, registrey_name, effect)
    

    class Permanent(metaclass=staticstr):
        all = list['PermanentEffect']()
        registered = list[str]()
      

        def __str__() -> str:
            rows = ""
            for effect in Effects.Instant.all:
                rows += f"{effect}\n"
            rows = rows.removesuffix("\n")
            return f"Permanent Effects:\n"\
                   f"{rows}"

        @staticmethod
        def register(effect:"TemporaryEffect", registrey_name:str):
            for registered_effect in Effects.Instant.all + Effects.Permanent.all + Effects.Temporary.all:
                registered_effect.uuid.compare(effect.uuid)
            Effects.Permanent.all.append(effect)
            Effects.Permanent.registered.append(effect.registry_name)
            setattr(Effects.Permanent, registrey_name, effect)
    

    class Catagories(metaclass=staticstr):
        all = list['EffectCategory']()
        registered = list[str]()
        

        def __str__() -> str:
            rows = ""
            for catagories in Effects.Catagories.all:
                rows += f"{catagories}\n"
            rows = rows.removesuffix("\n")
            return f"Effects Catagories:\n"\
                   f"{rows}"
    
        @staticmethod
        def register(category:"EffectCategory", registrey_name:str):
            for registered_catagory in Effects.Catagories.all:
                registered_catagory.uuid.compare(category.uuid)
            Effects.Catagories.all.append(category)
            Effects.Catagories.registered.append(category.registry_name)
            setattr(Effects.Catagories, registrey_name, category)


    @staticproperty
    def all_effects():
        return Effects.Instant.all + Effects.Temporary.all + Effects.Permanent.all


    def __str__():
        rows = ""
        i = len(Effects.Instant.all)
        t = len(Effects.Temporary.all)
        p = len(Effects.Permanent.all)
        while i > 0 or t > 0 or p > 0:
            temp = ""
            if i > 0:
                temp += f"{Effects.Instant.all[i-1].name}".center(20)
            else:
                temp += "                    "
            temp += "|"
            if t > 0:
                temp += f"{Effects.Temporary.all[t-1].name}".center(20)
            else:
                temp += "                    "
            temp += "|"
            if p > 0:
                temp += f"{Effects.Permanent.all[p-1].name}".center(20)
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
        self.__registry_name = None
        self.effects = list[Effect]()
    
    @property
    def uuid(self):
        return self.__uuid
    
    @property
    def registry_name(self):
        return self.__registry_name


    def __str__(self):
        instant_effects = list[InstantEffect]()
        temporary_effects = list[TemporaryEffect]()
        permanent_effects = list[PermanentEffect]()

        for effect in self.effects:
            if isinstance(effect, InstantEffect):
                effect.name += "instant"
                instant_effects.append(effect)
            elif isinstance(effect, TemporaryEffect):
                temporary_effects.append(effect)
            elif isinstance(effect, PermanentEffect):
                permanent_effects.append(effect)

        rows = ""
        i = len(instant_effects)
        t = len(temporary_effects)
        p = len(permanent_effects)
        while i > 0 or t > 0 or p > 0:
            temp = ""
            if i > 0:
                temp += f"{instant_effects[i-1].name}".center(20)
            else:
                temp += "                    "
            temp += "|"
            if t > 0:
                temp += f"{temporary_effects[t-1].name}".center(20)
            else:
                temp += "                    "
            temp += "|"
            if p > 0:
                temp += f"{permanent_effects[p-1].name}".center(20)
            else:
                temp += "                    "
            temp += "\n"
            
            i -= 1
            t -= 1
            p -= 1
            rows += temp

        return f"Effects in catagory: {self.name}:\n"\
               f"Instant Effects     |Temporary           |Permanent                    \n"\
               f"                    |                    |                    \n"\
               f"{rows}"\
               f"                    |                    |                    "
    

    def __format__(self, format_spec="default"):
        '''
        Options:\n
            \"effects\": returns a string of the effects\n
            \"catagories\": returns a string of the catagories\n
            \"description\": returns a string of the description\n
            \"name\": returns a string of the name\n
            \"uuid\": returns a string of the uuid

            does name by default
        '''
        match format_spec:
            case "effects":
                return ", ".join(self.methods)
            case "catagories":
                return ", ".join(self.catagory)
            case "description":
                return self.description
            case "name":
                return self.name
            case "uuid":
                return self.uuid
            case _:
                return self.name
        



    def add_effect(self, effect:"Effect"):
        self.effects.append(effect)

    

    def register(self, registrey_name:str):
        self.__registry_name = registrey_name
        Effects.Catagories.register(self, registrey_name)
        return self


class Effect:
    '''
This is a parent class and should not be used directly
    '''
    def __init__(self, uuid:UUID):
        self.__uuid = uuid
        self.name = "N/A"
        self.description = "N/A"
        self.__regitry_name = uuid.alphabetic_version
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
        return self


    def add_description(self, description:str):
        self.description = description
        return self


    def add_catagory(self, category:EffectCategory):
        getattr(category, "add_effect")(self)
        return self


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
  lycanthropey()
'''
        self.methods.append(args)
        return self


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
        return self




class InstantEffect(Effect):
    def __init__(self, uuid:UUID):
        super().__init__(uuid)
        self.__uuid = uuid
        self.__regitry_name = uuid.alphabetic_version
    
    @property
    def registry_name(self) -> str:
        return self.__regitry_name
    

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
    

    def __format__(self, format_spec:str="name"):
        '''
        Options:\n
            \"effects\": returns a string of the effects\n
            \"catagories\": returns a string of the catagories\n
            \"description\": returns a string of the description\n
            \"name\": returns a string of the name\n
            \"uuid\": returns a string of the uuid

            does name by default
        '''
        match format_spec:
            case "effects":
                return ", ".join(self.methods)
            case "catagories":
                return ", ".join(self.catagory)
            case "description":
                return self.description
            case "name":
                return self.name
            case "uuid":
                return self.uuid
            case _:
                return self.name
      

    def register(self, registry_name:str):
        if registry_name in Effects.Instant.registered:
            raise ValueError(f"Duplicate registry name \"{registry_name}\"")
        self.__regitry_name = registry_name
        Effects.Instant.register(self, registry_name)


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


    def release(self):
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


class TemporaryEffect(Effect):
    def __init__(self, uuid:UUID):
        super().__init__(uuid)
        self.__uuid = uuid
        self.__regitry_name = uuid.alphabetic_version
        self.duration = 0.0
        self.time_passed = .0
    
    @property
    def registry_name(self) -> str:
        return self.__regitry_name


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


    def __format__(self, format_spec:str="name"):
        '''
        Options:\n
            \"effects\": returns a string of the effects\n
            \"catagories\": returns a string of the catagories\n
            \"description\": returns a string of the description\n
            \"name\": returns a string of the name\n
            \"uuid\": returns a string of the uuid

            does name by default
        '''
        match format_spec:
            case "effects":
                return ", ".join(self.methods)
            case "catagories":
                return ", ".join(self.catagory)
            case "description":
                return self.description
            case "name":
                return self.name
            case "uuid":
                return self.uuid
            case _:
                return self.name


    def register(self, registry_name:str):
        if registry_name in Effects.Temporary.registered:
            raise ValueError(f"Duplicate registry name \"{registry_name}\"")
        self.__regitry_name = registry_name
        Effects.Temporary.register(self, registry_name)


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
        
        time_passed = self.time_passed
        if time_passed > self.duration:
            time_passed -= self.duration
        
        self.__setattr__(damage_type, self.__getattribute__(damage_type) - (amount*time_passed))
    

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

        time_passed = self.time_passed

        if time_passed > self.duration:
            time_passed -= self.duration

        self.__setattr__(heal_type, self.__getattribute__(heal_type) + (amount*time_passed))
        

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
    

    def hold(self, time_passed:float):
        self.duration -= time_passed
        self.time_passed = time_passed
        for method in self.methods:
          self.__getattribute__(method[0])(method)


    def release(self):
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


    def add_time(self, amount:float):
        self.duration += amount
    

    def remove_time(self, amount:float):
        self.duration -= amount


class PermanentEffect(Effect):
    def __init__(self, uuid:UUID):
        super().__init__(uuid)
        self.__uuid = uuid
        self.__regitry_name = uuid

        self.wereworlf = False
        self.end = False
    
    @property
    def registry_name(self) -> str:
        return self.__regitry_name


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


    def __format__(self, format_spec:str="name"):
        '''
        Options:\n
            \"effects\": returns a string of the effects\n
            \"catagories\": returns a string of the catagories\n
            \"description\": returns a string of the description\n
            \"name\": returns a string of the name\n
            \"uuid\": returns a string of the uuid

            does name by default
        '''
        match format_spec:
            case "effects":
                return ", ".join(self.methods)
            case "catagories":
                return ", ".join(self.catagory)
            case "description":
                return self.description
            case "name":
                return self.name
            case "uuid":
                return self.uuid
            case _:
                return self.name


    def register(self, registry_name:str):
        if registry_name in Effects.Permanent.registered:
            raise ValueError(f"Duplicate registry name \"{registry_name}\"")
        self.__regitry_name = registry_name
        Effects.Permanent.register(self, registry_name)
    

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
    

    def lycanthropey(self):
        '''
        this function should not be called directly, instead use the add_effect method

        no args
        '''
        self.wereworlf = True
            
    

    def trigger(self):
        for method in self.methods:
          self.__getattribute__(method[0])(method)
    
    def release(self):
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
        self.wereworlf = False