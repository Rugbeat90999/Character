
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
    @staticmethod
    def register_effect(name:str, effect_type:str, poison:bool):
        Effect()


class Effect:
    def __init__(self:"Effect", name:str, positive:bool):
        self.name = name
        self.positive = positive
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
        self.methods = list[list]()
    
    
    def trigger(self):
        for method_info in self.methods:
            self.__getattribute__()

class InstantEffect(Effect):
    def __init__(self, name:str):
        super().__init__(name, False)
    
    def damage(self, var_tuple:tuple[str, int]):
        damage_type:str = var_tuple[0]
        amount:int = var_tuple[1]
        if damage_type not in ["health", "stamina", "mana"]:
          raise ValueError(f"{damage_type}, is not damageable stat")
        self.__setattr__(damage_type, self.__getattribute__(damage_type) - amount)

    def heal(self, var_tuple:tuple[str, int]):
        heal_type:str = var_tuple[0]
        amount:int = var_tuple[1]
        if heal_type not in ["health", "stamina", "mana"]:
          raise ValueError(f"{heal_type}, is not healable stat")

        self.__setattr__(heal_type, self.__getattribute__(heal_type) + amount)
    
    def activate(self, methods: list[tuple[str | int]]):
        self.methods = methods
    
        
    

class TemporaryEffect(Effect):
    def __init__(self, name:str):
        super().__init__(name)
        self.duration = 0


class PermanantEffect(Effect):
    def __init__(self, name:str):
        super().__init__(name)




damage = InstantEffect("Damage")
# damage.damage("bob", 5)
# print(damage.bob)


damage.activate([["damage", "health", 2]])