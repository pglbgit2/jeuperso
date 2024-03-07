import armors, items, weapons, races, defaultSkills, interaction
from typing import List, Union, Dict
import random, copy, ast

FACTIONS = ["Heroes","Bandits"]


class CHARACTER:
    def __init__(self, name:str, faction:str, gold:int = 0, HP:int =20, MaxHP:int =20, Stamina:int =5, magic:int =0, stamina_regeneration:int =5, race :str = "Human",  Equipment: List[Union[armors.ARMOR, weapons.WEAPON, weapons.RANGE_WEAPON]] = [], Inventory: List[items.ITEM] = [], skills : List[str] = copy.copy(defaultSkills.DEFAULT_SKILLS), dodge : float = 0.15, skillsLevel : Dict[str,int] = {}):
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
            if skill not in defaultSkills.NOT_UPGRADABLE and skill in defaultSkills.DEFAULT_SKILLS :
                self.basicSkillsLevel[skill] = 1
        self.basicSkillsLevel = {**self.basicSkillsLevel, **skillsLevel}
        self.defensePoints = 0
        self.dodgePercent = dodge
        self.dodgeUsual = dodge
        self.actions = []
        self.isControlledByGM = True
        
    
    
    def newTurn(self):
        self.stamina = min(self.stamina +self.stamina_regeneration, self.MaxStamina)
        self.defensePoints = 0
        self.dodgePercent = self.dodgeUsual
        self.actions = []
        if self.HP < self.MaxHP/2:
            self.HP -= 1
    
    def getEstimatedPower(self):
        return self.HP
    
    def setUpActions(self, fightersByName : Dict[str, 'CHARACTER'], teamEstimatedPower : Dict[str,int], fightersByFaction : Dict[str,List['CHARACTER']]):
        if self.isControlledByGM:
            self.actions = interaction.getPlayerActions(self.name, fightersByName.keys(), self.skills)
            return self.actions
        else:
            actions = []
            staminaCost = 0
            if self.HP < self.MaxHP /2:
                attackProbability = 0.4
            else: 
                attackProbability = 0.6
                
            if all(teamEstimatedPower[self.faction] <= teamEstimatedPower[enemy] for enemy in teamEstimatedPower.keys()):
                attackProbability -= 0.2
                
            while staminaCost < self.stamina:
                action = {}
                leftHandUsed = False
                rightHandUsed = False
                
                if random.random() <= attackProbability:
                    action["name"] = random.choice([defaultSkills.CA, defaultSkills.QA])
                    action["target"] = random.choice(random.choice([team for team in teamEstimatedPower.keys() if team != self.faction]))
                    if not leftHandUsed: 
                        action["hand"] = "left"
                    else:
                        if not rightHandUsed:
                            action["hand"] = "right"
                        else:
                            action = None
                else:
                    action["name"] = defaultSkills.CD
                    action["target"] = self.name
                if action != None:
                    actions.append(action)
                    staminaCost += defaultSkills.DEFAULT_SKILLS_COST[action]
            if staminaCost > self.stamina:
                actions.pop()
                while staminaCost != self.stamina:
                    actions.append({"name" : defaultSkills.LD, "target" : self.name})
                    staminaCost += 1
            self.actions = actions
            return actions
                
    
    def max_weight(self):
        return self.stamina*30
    
    def getItemFromInventoryByName(self, name : str):
        for item in self.inventory:
            if item.name == name:
                return item
        return None
        
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
            if stuff != None:
                self.equip(stuff)
            
            
    def total_weight(self):
        if self.weight == 0:
            for item in self.inventory:
                self.weight += item.weight
        return self.weight
    
    def get_speed(self):
        return (self.max_weight() - self.total_weight())/10
            
    def put_into_inventory(self, stuff : items.ITEM):
        if stuff != None:
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
            return "lv-"+str(self.basicSkillsLevel[skillName])
        else:
            return ""
    
    def dodge(self):
        if self.dodgePercent > 0:
            return random.randint(0,100) <= self.dodgePercent
        else:
            return False
    
    
    def isEquipped(self, item : Union[weapons.WEAPON, weapons.RANGE_WEAPON, armors.ARMOR]):
        return item == self.bodyArmor or item == self.leftTool or item == self.legsArmor or item == self.headArmor or item == self.rightTool
    
    def getDictInfos(self):
        fighterDict = { 
            "HP" : self.HP,
            "MaxHP" : self.MaxHP,
            "magic" : self.magic,
            "gold" : self.money,
            "stamina_regeneration" : self.stamina_regeneration,
            "dodge" : self.dodgeUsual
        }
        if self.inventory != []:
            fighterDict["Inventory"] = {}
            fighterDict["Inventory"]["weapons"] = []
            fighterDict["Inventory"]["armors"] = []
            fighterDict["Inventory"]["items"] = []
            for item in (self.inventory):
                if isinstance(item, weapons.WEAPON) or isinstance(item, weapons.RANGE_WEAPON):
                    fighterDict["Inventory"]["weapons"].append((item.name, self.isEquipped(item)))
                else:
                    if isinstance(item,armors.ARMOR):
                        fighterDict["Inventory"]["armors"].append((item.name, self.isEquipped(item)))
                    else: 
                        fighterDict["Inventory"]["weapons"].append(item.name)
        return fighterDict
    
    def saveFighter(self, filename : str):
        path = "./characters/"+filename
        try:
            with open(path, "w+") as file:
                fighterDict = self.getDictInfos()
                file.write(self.name+"\n")
                file.write(self.faction+"\n")
                file.write(str(fighterDict)+"\n")
                file.close()
        except Exception as e:
            print(e.args)
            interaction.throwError("problem while saving "+self.name)

    @staticmethod
    def retrieveFighter(filename : str):
        path = "./characters/"+filename
        try:
            with open(path, "r") as file:
                NameLine = file.readline()[:-1]
                factionLine = file.readline()[:-1]
                dictLine = file.readline()[:-1]
                if dictLine != None:
                    fighterDictStr = ast.literal_eval(dictLine)
                    if isinstance(fighterDictStr, Dict):
                        file.close()
                        print(factionLine)
                        return CHARACTER.instantiate_from_dict(name=NameLine, faction=factionLine, Race=fighterDictStr)
                    else:
                        file.close() 
                        return None
                else:
                    file.close()
                    return None
        except Exception as e:
            print(e.args)
            interaction.throwError("file "+filename+" do not exist")
    
    @staticmethod
    def instantiate_from_dict(Race : Dict, name : str, faction : str):
        if faction in FACTIONS:
            if "Inventory" in Race.keys():
                    Race["Equipment"] = []
                    Inventory = []
                    if "weapons" in Race["Inventory"].keys():
                        for weapon in Race["Inventory"]["weapons"]:
                            toEquip = weapon[1]
                            if weapon[0] in weapons.MELEE_WEAPONS:
                                weapon = weapons.WEAPON.get_melee_weapon(weapon[0])
                                if weapon != None:
                                    Inventory.append(weapon)
                                    if toEquip:
                                        Race["Equipment"].append(weapon)
                                    
                            elif weapon[0] in weapons.RANGE_WEAPONS:
                                toEquip = weapon[1]
                                weapon = weapons.RANGE_WEAPON.get_range_weapon(weapon[0])
                                if weapon != None:
                                    Inventory.append(weapon)
                                    if toEquip:
                                        Race["Equipment"].append(weapon)
                    if "armors" in Race["Inventory"].keys():
                        for armor in Race["Inventory"]["armors"]:
                            print(armor)
                            toEquip = armor[1]
                            armor = armors.ARMOR.get_armor(armor[0])
                            if armor != None:
                                Inventory.append(armor)
                                if toEquip and armor != None:
                                    Race["Equipment"].append(armor)
                    if "items" in Race["Inventory"].keys():            
                        for item in Race["Inventory"]["items"]:
                            item = items.ITEM.get_item(item)
                            if item != None:
                                Inventory.append(item)
                    Race["Inventory"] = Inventory
            return CHARACTER(name = name, faction = faction, **Race)
        else: 
            interaction.throwError("faction do not exist")
            return None


    @staticmethod
    def instantiate_from_race(race:str, name:str, faction: str):
        if race in races.RACES :
            Race = copy.copy(getattr(races, race))
            return CHARACTER.instantiate_from_dict(Race, name, faction)
        else : 
            interaction.throwError("Race do not exist, create it and add it to race & class array")
            return None
            
        
# billy = CHARACTER.instantiate_from_race("CITY_GARD", "billy", "Heroes")
# billy.saveFighter("billy.sav")
# billy2 = CHARACTER.retrieveFighter("billy.sav")
# print(billy2.inventory)