import armors, items, weapons, races, defaultSkills, interaction, consumable
from typing import List, Union, Dict
import random, copy, ast, math

FACTIONS = ["Players","Enemies"]


class CHARACTER:
    def __init__(self, name:str, faction:str, gold:int = 0, HP:int =20, MaxHP:int =20, Stamina:int =5, magic:int =0, stamina_regeneration:int =5, race :str = "HUMAN",  Equipment: List[Union[armors.ARMOR, weapons.WEAPON, weapons.RANGE_WEAPON]] = [], Inventory: List[items.ITEM] = [], skills : List[str] = list(defaultSkills.DEFAULT_SKILLS.keys())+defaultSkills.NOT_UPGRADABLE, dodge : float = 0.15, skillsLevel : Union[Dict[str,int], str] = {}, shotBonus : float = 0, raceResistance : Dict[str,float] = None, default_damage :int = 2, default_damage_type:int = "impact", tempDefByTurn : int =0):
        self.HP = HP
        self.MaxHP = MaxHP
        self.stamina = Stamina
        self.MaxStamina = Stamina
        self.magic = magic
        self.MaxMagic = magic
        self.stamina_regeneration = stamina_regeneration
        self.inventory = Inventory
        self.bodyArmor = None
        self.legsArmor = None
        self.leftTool = None
        self.rightTool = None
        self.headArmor = None
        self.equipAll(Equipment, begin=True)
        self.race = race
        self.name = name
        self.money = gold
        self.faction = faction
        self.weight = 0
        self.default_damage = default_damage
        self.default_damage_type = default_damage_type
        self.skills = skills
        if not isinstance(self.skills, List):
            self.skills = list(self.skills)
        
        self.basicSkillsLevel = {}
        for skill in skills:
            if skill not in defaultSkills.NOT_UPGRADABLE and skill in defaultSkills.DEFAULT_SKILLS.keys() :
                self.basicSkillsLevel[skill] = 1
        if isinstance(skillsLevel,str):
            skillsLevel = ast.literal_eval(skillsLevel)
        self.basicSkillsLevel.update(skillsLevel)
        self.resistance = copy.copy(races.DEFAULT_RESISTANCE)
        if raceResistance != None:
            self.resistance.update(raceResistance)
        self.defensePoints = 0
        self.dodgePercent = max(getattr(races, race)["dodge"], dodge)
        self.dodgeUsual = self.dodgePercent
        self.actions = []
        self.isControlledByGM = True
        self.shotBonus = shotBonus
        self.defenseByTurn = tempDefByTurn
        
    
    
    def newTurn(self):
        self.stamina = min(self.stamina +self.stamina_regeneration, self.MaxStamina)
        self.defensePoints = self.defenseByTurn
        self.magic = min(self.magic +self.stamina_regeneration, self.MaxMagic)
        self.dodgePercent = self.dodgeUsual
        self.actions = []
        if self.HP < self.MaxHP/2:
            self.HP -= 1
            
    
    def canHealItself(self):
        for item in self.inventory:
            if isinstance(item,consumable.Consumable):
                if item.canHeal():
                    return True
        return False
    
    def itemToHealItself(self):
        for item in self.inventory:
            if isinstance(item,consumable.Consumable):
                if item.canHeal():
                    return item
        return None
    
    
    def rollInRange(self,a:int,b:int):
        return random.randint(min([a,b]), max([a,b]))    
    
    
    def consumeConsumable(self, item: consumable.Consumable):
        if "Health" in item.effect.keys():
            (minHp, maxHP) = item.effect["Health"]
            recovery = self.rollInRange(minHp,maxHP)
            self.HP += recovery
            if recovery > 0:
                interaction.showInformation(self.name+" healed by "+str(recovery)+" HP using "+item.name)
            else:
                interaction.showInformation(self.name+" injured by "+str(recovery)+" HP using "+item.name) 
    
    
    def useConsumable(self, consumableName):
        for item in self.inventory:
            if item.name == consumableName:
                self.consumeConsumable(item)
                self.inventory.remove(item)
                return
    
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
                item = self.itemToHealItself()
                if item != None:
                    # must change this by adding action and cost
                    self.useConsumable(item.name)

            if self.HP < self.MaxHP /2:
                attackProbability = 0.4
            else: 
                attackProbability = 0.6
                
            if all(teamEstimatedPower[self.faction] <= teamEstimatedPower[enemy] for enemy in teamEstimatedPower.keys()):
                attackProbability -= 0.2
            leftHandUsed = self.leftTool == None
            rightHandUsed = self.rightTool == None
            while staminaCost < self.stamina:
                action = {}
               
                if not (leftHandUsed and rightHandUsed) and random.random() <= attackProbability:
                    action["targets"] = [random.choice(fightersByFaction[random.choice([team for team in teamEstimatedPower.keys() if team != self.faction])]).name]
                    if not leftHandUsed: 
                        action["hand"] = "left"
                        leftHandUsed = True
                        tool = self.leftTool
                    else:
                        action["hand"] = "right"
                        rightHandUsed = True
                        tool = self.rightTool
                    
                    if tool.name in weapons.MELEE_WEAPONS:
                            action["name"] = random.choice([defaultSkills.CA, defaultSkills.QA, defaultSkills.BA])
                    else:
                        if tool.name in weapons.RANGE_WEAPONS:
                            action["name"] = random.choice([defaultSkills.QS, defaultSkills.CS, defaultSkills.PS])
                        else:
                            interaction.throwError("Problem in game logic")
                else:
                    action["name"] = defaultSkills.CD
                    action["target"] = self.name
                if action != None:
                    actions.append(action)
                    staminaCost += defaultSkills.DEFAULT_SKILLS[action["name"]][self.basicSkillsLevel[action["name"]]]["StaminaCost"]
            while staminaCost > self.stamina:
                removed = actions.pop()
                staminaCost -= defaultSkills.DEFAULT_SKILLS[removed["name"]][self.basicSkillsLevel[action["name"]]]["StaminaCost"]
            while staminaCost != self.stamina:
                actions.append({"name" : defaultSkills.LD, "target" : self.name})
                staminaCost += 1
            self.actions = actions
            return actions
                

    def upgradeSkill(self, skill):
        self.basicSkillsLevel[skill] += 1
        interaction.showInformation("skill "+skill+" upgraded to level "+self.basicSkillsLevel[skill])
        
    def max_weight(self):
        return self.stamina*50
    
    def getItemFromInventoryByName(self, name : str):
        for item in self.inventory:
            if item.name == name:
                return item
        return None
      
        
    def equip(self, stuff : Union[armors.ARMOR, weapons.WEAPON, weapons.RANGE_WEAPON], side="left", beginningEquipping = False):
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
            if isinstance(stuff, weapons.WEAPON) or isinstance(stuff, weapons.RANGE_WEAPON):
                if stuff.name in weapons.TWO_HAND_WEAPONS:
                    self.leftTool = stuff
                    self.rightTool = stuff
                    return
                else :
                    if stuff.name in weapons.ONE_HAND_WEAPONS:
                        if side == "left":
                            if self.leftTool == None or not beginningEquipping:
                                self.leftTool = stuff
                                if self.rightTool in weapons.TWO_HAND_WEAPONS:
                                    self.rightTool = None
                                return
                        self.rightTool = stuff
                        if self.leftTool in weapons.TWO_HAND_WEAPONS:
                            self.leftTool = None
                    else:
                        interaction.throwError("weapon neither in one hand weapon or two hand weapon")
    
    def protection_damage(self, damage : int, damage_type:str, protection : armors.ARMOR):
        damage = protection.damage_absorption(damage, damage_type)
        if protection.durability == 0:
            protection = None
        return damage
    
    def take_damage(self, damage : float, damage_type : str):
        damage = math.floor(damage)
        race_reduction = damage*self.resistance[damage_type]
        if race_reduction > 0 and race_reduction < 1:
            race_reduction += 1
        elif race_reduction < 0 and race_reduction > -1: race_reduction -= 1
        damage -= race_reduction
        interaction.showInformation("damage of type "+damage_type+" reduced by "+str(self.resistance[damage_type]*100)+" percent because is "+self.race)
        if damage > 0:
            if self.defensePoints < 0:
                damage = damage / -self.defensePoints
            else:
                defense = self.defensePoints
                if defense > 0:
                    oldDamage = damage
                    damage = max(0, damage - self.defensePoints)
                    dif = oldDamage - damage
                    interaction.showInformation("damage reduced by temporary armor by:"+str(dif))
                    self.defensePoints -= dif
            if self.headArmor != None and damage > 0:
                damage = self.protection_damage(damage, damage_type , self.headArmor)
            if self.bodyArmor != None and damage > 0:
                damage = self.protection_damage(damage, damage_type, self.bodyArmor)
            if self.legsArmor != None and damage > 0:
                damage = self.protection_damage(damage, damage_type, self.legsArmor)
            damage = math.floor(damage)
            interaction.showInformation("fighter "+self.name+" took "+str(damage)+" damage")
            self.HP -= damage
    
    def equipAll(self, loadsOfStuff : List[Union[armors.ARMOR, weapons.WEAPON, weapons.RANGE_WEAPON]], begin=False):
        for stuff in loadsOfStuff:
            if stuff != None:
                self.equip(stuff,beginningEquipping=begin)
            
            
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
                interaction.showInformation(stuff.name+" added to "+self.name+" inventory")
            else:
                interaction.showInformation("Too much weight")
    
    def lootAll(self, loot: List[items.ITEM]):
        for item in loot:
            self.put_into_inventory(item)

    def getInitiative(self):
        return random.randint(0,100)
    
    def addSkill(self, skill:str, Upgradable = False):
        if skill not in self.skills:
            self.skills.append(skill)
            interaction.showInformation("learned new skill: "+skill)
            if Upgradable:
                self.basicSkillsLevel[skill] = 1
            return True
        return False
            
    def useSkill(self,skill:str):
        pass
    
    def getStrLevelOfSkill(self, skillName : str):
        if skillName in self.basicSkillsLevel.keys():
            return "-lv"+str(self.basicSkillsLevel[skillName])
        else:
            return ""
    
    def dodge(self,modification=0):
        if self.dodgePercent > 0:
            val = random.randint(0,100) <= self.dodgePercent + modification
            if val:
                self.dodgePercent -= 0.1
            return val
        else:
            return False
    
    
    def isEquipped(self, item : Union[weapons.WEAPON, weapons.RANGE_WEAPON, armors.ARMOR]):
        return item == self.bodyArmor or item == self.leftTool or item == self.legsArmor or item == self.headArmor or item == self.rightTool
        
    def removeItemFromInventoryByName(self, itemName: str):
        for item in self.inventory:
            if item.name == itemName:
                self.inventory.remove(item)
                if isinstance(item, Union[weapons.WEAPON, weapons.RANGE_WEAPON, armors.ARMOR]) and self.isEquipped(item):
                    match item.name:
                        case self.bodyArmor:
                            self.bodyArmor = None
                        case self.leftTool:
                            self.leftTool = None
                        case self.rightTool:
                            self.rightTool = None
                        case self.legsArmor:
                            self.legsArmor = None
                        case self.headArmor:
                            self.headArmor = None
                return item
        return None
        
    def shot(self, accuracy : int):
        return random.random() <= accuracy + self.shotBonus
        
        
    def getDictInfos(self):
        fighterDict = { 
            "HP" : self.HP,
            "MaxHP" : self.MaxHP,
            "magic" : self.magic,
            "gold" : self.money,
            "stamina_regeneration" : self.stamina_regeneration,
            "dodge" : self.dodgeUsual,
            "shotBonus" : self.shotBonus,
            "skills" : self.skills,
            "skillsLevel" : str(self.basicSkillsLevel),
            "tempDefByTurn" : self.defenseByTurn
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
                        fighterDict["Inventory"]["armors"].append((item.name, self.isEquipped(item),item.durability))
                    else:
                        fighterDict["Inventory"]["items"].append(item.name)
        return fighterDict
    
    def saveFighter(self, filename : str):
        path = "./characters/"+filename
        try:
            with open(path, "w+") as file:
                fighterDict = self.getDictInfos()
                file.write(self.name+"\n")
                file.write(self.faction+"\n")
                file.write(self.race+"\n")
                file.write(str(fighterDict)+"\n")
                file.close()
        except Exception as e:
            print(e.args)
            interaction.throwError("problem while saving "+self.name)
    
    def checkForUpgrades(self):
        pass

    @staticmethod
    def retrieveFighter(filename : str):
        path = "./characters/"+filename
        try:
            with open(path, "r") as file:
                NameLine = file.readline()[:-1]
                factionLine = file.readline()[:-1]
                raceLine = file.readline()[:-1]
                dictLine = file.readline()[:-1]
                if dictLine != None:
                    fighterDictStr = ast.literal_eval(dictLine)
                    file.close()
                    if isinstance(fighterDictStr, Dict):
                        return CHARACTER.instantiate_from_dict(name=NameLine, faction=factionLine, classAttributes=fighterDictStr, race=raceLine)
                    else:
                        return None
                else:
                    file.close()
                    return None
        except Exception as e:
            print(e.args)
            interaction.throwError("file "+filename+" do not exist or has not correct format")
    
    
    
    @staticmethod
    def instantiateInventoryEquipment(Race):
        if "Inventory" in Race.keys():
                    Race["Equipment"] = []
                    Inventory = []
                    if "weapons" in Race["Inventory"].keys():
                        for weapon in Race["Inventory"]["weapons"]:
                            if weapon[0] == "random":
                                weapon_name = random.choice(weapon[2])
                                #print(weapon_name)
                            else: weapon_name = weapon[0]
                                
                            toEquip = weapon[1]
                            if weapon_name in weapons.MELEE_WEAPONS:
                                weapon = weapons.WEAPON.get_melee_weapon(weapon_name)
                                if weapon != None:
                                    Inventory.append(weapon)
                                    if toEquip:
                                        Race["Equipment"].append(weapon)
                                    
                            else :
                                if weapon_name in weapons.RANGE_WEAPONS:
                                    toEquip = weapon[1]
                                    weapon = weapons.RANGE_WEAPON.get_range_weapon(weapon_name)
                                    if weapon != None:
                                        Inventory.append(weapon)
                                        if toEquip:
                                            Race["Equipment"].append(weapon)
                            
                                elif weapon_name in weapons.RANGE_PROJECTILE:
                                    if len(weapon) == 3:
                                        number = weapon[2]
                                    else:
                                        number = 1
                                    weapon = weapons.WEAPON.get_munition_weapon(weapon[0])
                                    if weapon != None:
                                        for _ in range(number):
                                            Inventory.append(copy.copy(weapon))
                                    
                    if "armors" in Race["Inventory"].keys():
                        for strArmor in Race["Inventory"]["armors"]:
                            toEquip = strArmor[1]
                            
                            armor = armors.ARMOR.get_armor(strArmor[0])
                            if len(strArmor) == 3:
                                durability = strArmor[2]
                                armor.durability = durability
                            if armor != None:
                                Inventory.append(armor)
                                if toEquip and armor != None:
                                    Race["Equipment"].append(armor)
                    if "items" in Race["Inventory"].keys():            
                        for item in Race["Inventory"]["items"]:
                            if item in consumable.CONSUMABLE:
                                item = consumable.Consumable.get_consumable(item)
                            else:
                                item = items.ITEM.get_item(item)
                            if item != None:
                                Inventory.append(item)
                    Race["Inventory"] = Inventory
    
    @staticmethod
    def instantiate_from_dict(classAttributes : Dict, name : str, faction : str, race:str):
        if faction in FACTIONS:
            if race in races.RACES:
                CHARACTER.instantiateInventoryEquipment(classAttributes)
                Race = copy.copy(getattr(races, race))
                return CHARACTER(name = name, faction = faction, race=race, raceResistance=Race["raceResistance"], **classAttributes)
            else: 
                interaction.throwError("Race do not exist, create it and add it to race array")
        else: 
            interaction.throwError("faction do not exist")
            return None

    

    @staticmethod
    def instantiate_from_class(characterClass:str, name:str, faction: str, race:str):
        if characterClass in races.CLASSES:
            if characterClass != "DEFAULT_CLASS":
                classAttributes = copy.copy(getattr(races, characterClass))
            else:
                classAttributes = copy.copy(getattr(races, race))
                del classAttributes["race"]
                del classAttributes["raceResistance"]

            return CHARACTER.instantiate_from_dict(classAttributes, name, faction,race)
        else : 
            interaction.throwError("Class do not exist, create it and add it to class array")
            return None
    
    
    @staticmethod
    def getListOfItemFromStr(stringList, itemType=""):
        if itemType == "weapons":
            fighterWeapons = []
            for weapon_name in stringList:
                if weapon_name in weapons.MELEE_WEAPONS:
                    fighterWeapons.append(weapons.WEAPON.get_melee_weapon(weapon_name))
                else:
                    if weapon_name in weapons.RANGE_WEAPONS:
                        fighterWeapons.append(weapons.RANGE_WEAPON.get_range_weapon(weapon_name))
                    else:
                        if weapon_name in weapons.RANGE_PROJECTILE:
                            fighterWeapons.append(weapons.WEAPON.get_munition_weapon(weapon_name))    
                        else:
                            interaction.throwError("given weapon do not exist")
            return fighterWeapons
                            
        if itemType == "armors":
            fighterArmors = []
            for armor_name in stringList:
                if armor_name in armors.ARMORS:
                    fighterArmors.append(armors.ARMOR.get_armor(armor_name))
                else: interaction.throwError("given armor do not exist")
            return fighterArmors
        
        if itemType == "items":
            Inventory = []
            for item_name in stringList:
                if item_name in consumable.CONSUMABLE:
                    item = consumable.Consumable.get_consumable(item)
                else:
                    item = items.ITEM.get_item(item)
                if item != None:
                    Inventory.append(item)
            return Inventory
    
    @staticmethod
    def getCharacterInfos():
        
        infos = {}
        
        infos["name"] = input("name:\n")
        
        race = "nope"
        while race not in races.RACES:
            race = input("race: \n")
        infos["race"] = race
        
        for value in ["gold", "HP", "MaxHP","magic","Stamina", "stamina_regeneration"]:
            infos[value] = interaction.askForInt(value+":\n")
                
        fighterFaction = "nope"
        while fighterFaction not in FACTIONS:
            fighterFaction = input("faction: \n")
        infos["faction"] = fighterFaction
        
        inventoryChecked = False
        fighterInventory = []
        for itemType in ["weapons", "armors", "items"]:
            itemList = None
            itemStrList = []
            while itemList == None or len(itemList) != len(itemStrList):
                item = input(itemType+"\n")
                if item != "" and item != "\n":
                    if " " in item:
                        itemStrList = item.split(" ")
                    else: itemStrList = [item]
                    itemList = CHARACTER.getListOfItemFromStr(itemStrList, itemType)
                else:
                    itemList = []
            fighterInventory.extend(itemList)
        infos["Inventory"] = fighterInventory
        skillsLevel = {}
        for skill in defaultSkills.DEFAULT_SKILLS:
            skillsLevel[skill] = interaction.askForInt(skill+" level: \n")
        infos["skillsLevel"] = skillsLevel
        return infos
                
                
                
            
            
          
                
            
            
# billy = CHARACTER.instantiate_from_class("WARRIOR", "billy", "Heroes", "HUMAN")
# billy.inventory.append(consumable.Consumable.get_consumable("HEALTH_POTION"))
# billy.inventory.append(consumable.Consumable.get_consumable("HEALTH_POTION"))
# print(billy.inventory)
# billy.HP=3
# billy.useConsumable("HEALTH_POTION")
# print(billy.HP)
# print(billy.dodgePercent)
# print(billy.inventory)
# billy.saveFighter("billy.sav")
# billy2 = CHARACTER.retrieveFighter("billy.sav")
# print(billy2.inventory)