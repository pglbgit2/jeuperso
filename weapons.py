


## DEFAULT SWORD ATTRIBUTES ##

SWORD_DAMAGE = 9
SWORD_WEIGHT = 20
SWORD_COST = 40 
SWORD_SPEED = 15
SWORD = (SWORD_DAMAGE, SWORD_WEIGHT, SWORD_COST, SWORD_SPEED)

## DEFAULT KNIFE ATTRIBUTES ##

KNIFE_DAMAGE = 5
KNIFE_WEIGHT = 7
KNIFE_COST = 10
KNIFE_SPEED = 25
KNIFE = (KNIFE_DAMAGE, KNIFE_WEIGHT, KNIFE_COST, KNIFE_SPEED)


## DEFAULT LONG_SWORD ATTRIBUTES ##

LONG_SWORD_DAMAGE = 12
LONG_SWORD_WEIGHT = 35
LONG_SWORD_COST = 70
LONG_SWORD_SPEED = 5
LONG_SWORD = (LONG_SWORD_DAMAGE, LONG_SWORD_WEIGHT, LONG_SWORD_COST, LONG_SWORD_SPEED)

## DEFAULT SPIKED_CLUB ATTRIBUTES ##

SPIKED_CLUB_DAMAGE = 7
SPIKED_CLUB_WEIGHT = 14
SPIKED_CLUB_COST = 15
SPIKED_CLUB_SPEED = 18
SPIKED_CLUB = (SPIKED_CLUB_DAMAGE, SPIKED_CLUB_WEIGHT, SPIKED_CLUB_COST, SPIKED_CLUB_SPEED)

class WEAPON:
    def __init__(self, _cost : int, _damage : int, _weight : int, _speed : int):
        self.cost = _cost
        self.damage =_damage
        self.weight = _weight
        self.speed = _speed
        
    def upgrade(self, damage_boost : int):
        self.damage += damage_boost
    
    @staticmethod
    def get_weapon(weapon_name):
        if weapon_name in globals():
            (WEAPON_DAMAGE, WEAPON_WEIGHT, WEAPON_COST, WEAPON_SPEED) = globals()[weapon_name]
            return WEAPON(WEAPON_DAMAGE, WEAPON_WEIGHT, WEAPON_COST, WEAPON_SPEED)
        else:
            print("No Weapon with such name")
            return None
    
        

