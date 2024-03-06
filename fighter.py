import armors, items, weapons, races, defaultSkills
from typing import List, Union, Dict
import random, copy

FACTIONS = ["Heroes","Bandits","City"]


class CHARACTER:
    def __init__(self, name:str, faction:str, gold:int = 0, HP:int =20, MaxHP:int =20, Stamina:int =5, magic:int =0, stamina_regeneration:int =5, race :str = "Human",  Equipment: List[Union[armors.ARMOR, weapons.WEAPON, weapons.RANGE_WEAPON]] = [], Inventory: List[items.ITEM] = [], skills : List[str] = copy.copy(defaultSkills.DEFAULT_SKILLS), dodge : float = 0.15, skillsLevel : Dict[str:int] = {}):
        self.HP = HP
        self.MaxHP = MaxHP
        self.stamina = Stamina
        self.MaxStamina = Stamina
        self.magic = magic
        self.stamina_regeneration = stamina_regeneration
        self.inventory = Inventory
        self.bodyArmor = None
        self.legsArmor = None
        self.leftTool = None
        self.rightTool = None
        self.headArmor = None
        self.equipAll(Equipment)
        self.race = race
        self.name = name
        self.money = gold
        self.faction = faction
        self.weight = 0
        self.skills = skills
        self.basicSkillsLevel = {}
        for skill in skills:
            if skill != "Equip" and skill in defaultSkills.DEFAULT_SKILLS :
                self.basicSkillsLevel[skill] = 1
        self.basicSkillsLevel = {**self.basicSkillsLevel, **skillsLevel}
        self.defensePoints = 0
        self.dodgePercent = dodge
        self.dodgeUsual = dodge
        self.actions = []
    
    
    def newTurn(self):
        self.stamina = min(self.stamina +self.stamina_regeneration, self.MaxStamina)
        self.defensePoints = 0
        self.dodgePercent = self.dodgeUsual
        self.actions = []
    
    def setUpActions(self, fightersNames : List[str]):
        pass
    
    def max_weight(self):
        return self.stamina*30
        
    def equip(self, stuff : Union[armors.ARMOR, weapons.WEAPON, weapons.RANGE_WEAPON], side="left"):
        if stuff in self.inventory:
            if isinstance(stuff, armors.ARMOR):
                if stuff.name in armors.BODY:
                    self.bodyArmor = stuff
                    return
                if stuff.name in armors.HEAD:
                    self.headArmor = stuff
                    return
                if stuff.name in armors.LEGS:
                    self.legsArmor = stuff
                    return
                
            if stuff.name in weapons.TWO_HAND_WEAPONS:
                self.leftTool = stuff
                self.rightTool = stuff
                return
            else:
                if side == "left":
                    self.leftTool = stuff
                    return
                self.rightTool = stuff
    
    def protection_damage(self, damage : int, damage_type:str, protection : armors.ARMOR):
        damage = protection.damage_absorption(damage, damage_type)
        if protection.durability == 0:
            protection = None
        return damage
    
    def take_damage(self, damage : int, damage_type : str):
        if self.defensePoints < 0:
            damage = damage / -self.defensePoints
        else:
            damage -= self.defensePoints
        if self.headArmor != None and damage > 0:
            damage = self.protection_damage(damage, damage_type , self.headArmor)
        if self.bodyArmor != None and damage > 0:
            damage = self.protection_damage(damage, damage_type, self.bodyArmor)
        if self.legsArmor != None and damage > 0:
            damage = self.protection_damage(damage, damage_type, self.legsArmor)
        self.HP -= damage
    
    def equipAll(self, loadsOfStuff : List[Union[armors.ARMOR, weapons.WEAPON, weapons.RANGE_WEAPON]]):
        for stuff in loadsOfStuff:
            self.equip(stuff)
            
            
    def total_weight(self):
        if self.weight == 0:
            for item in self.inventory:
                self.weight += item.weight
        return self.weight
    
    def get_speed(self):
        return (self.max_weight() - self.total_weight())/10
            
    def put_into_inventory(self, stuff : items.ITEM):
        if self.total_weight() <= self.max_weight() and stuff not in self.inventory:
            self.inventory.append(stuff)
            self.weight += stuff.weight
    
    def lootAll(self, loot: List[items.ITEM]):
        for item in loot:
            self.put_into_inventory(item)

    def getInitiative(self):
        return random.randint(0,100)
    
    def addSkill(self, skill:str, Upgradable = False):
        if skill not in self.skills:
            self.skills.append(skill)
            if Upgradable:
                self.basicSkillsLevel[skill] = 1
            return True
        return False
            
    def useSkill(self,skill:str):
        pass
    
    def getStrLevelOfSkill(self, skillName : str):
        if skillName in self.basicSkillsLevel.keys():
            return "lv-"+self.basicSkillsLevel[skillName]
        else:
            return ""
    
    def dodge(self):
        if self.dodgePercent > 0:
            return random.randint(0,100) <= self.dodgePercent
        else:
            return False
    @staticmethod
    def instantiate_from_race(race:str, name:str, faction: str):
        if race in races.RACES and faction in FACTIONS:
            Race = getattr(races, race)
            return CHARACTER(name = name, faction = faction, **Race)
        
# billy = CHARACTER.instantiate_from_race("HUMAN", "billy", "Heroes")
# print(billy.faction)