import items


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

## IRON ARROW ##

ARROW_DAMAGE = 5
ARROW_WEIGHT = 0.2
ARROW_COST = 0.3
ARROW_SPEED = 10
ARROW = (ARROW_DAMAGE, ARROW_WEIGHT, ARROW_COST, ARROW_SPEED)

## ROCK ##
ROCK_DAMAGE = 3
ROCK_WEIGHT = 0.7
ROCK_COST = 0
ROCK_SPEED = 10
ROCK = (ROCK_DAMAGE, ROCK_WEIGHT, ROCK_COST, ROCK_SPEED)

## SPEAR ##

SPEAR_DAMAGE = 6
SPEAR_WEIGHT = 12
SPEAR_COST = 20
SPEAR_SPEED = 12
SPEAR = (SPEAR_DAMAGE, SPEAR_WEIGHT, SPEAR_COST, SPEAR_SPEED)

## RANGE AMMO ##

RANGE = ["ARROW", "ROCK"]

## THROWABLE ##

THROWABLE = ["KNIFE", "ROCK", "SPEAR"]

class WEAPON(items.ITEM):
    def __init__(self, _cost : int, _damage : int, _weight : int, _speed : int):
        super().__init__(_cost,_weight)
        self.damage =_damage
        self.speed = _speed
        
    def upgrade(self, damage_boost : int):
        self.damage += damage_boost
    
    @staticmethod
    def get_melee_weapon(weapon_name):
        if weapon_name in globals():
            (WEAPON_DAMAGE, WEAPON_WEIGHT, WEAPON_COST, WEAPON_SPEED) = globals()[weapon_name]
            return WEAPON(WEAPON_DAMAGE, WEAPON_WEIGHT, WEAPON_COST, WEAPON_SPEED)
        else:
            print("No Weapon with such name")
            return None
    
        

