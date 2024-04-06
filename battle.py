import fighter, rules, action, player, interaction, items, readline, weapons, defaultSkills
from typing import List, Dict, Union, Tuple

class Battle:
    def __init__(self, fighters : List[fighter.CHARACTER]):
        assert not any(fighter1.name == fighter2.name for fighter1 in fighters for fighter2 in fighters if fighter1 != fighter2)
        if action.Action.ACTIONS_DICT == {}:
            action.setupActions()
        if action.Action.ACTIONS_DICT == {} or fighters == []:
            raise Exception("Can not start battle")
        self.fighters = fighters
        self.fightersNames : Dict[str, fighter.CHARACTER] = {}
        self.factionsWarriors : Dict[str,List[str]] = {}
        self.defeatedWarriors : List[fighter.CHARACTER] = []
        for warrior in fighters:
            self.fightersNames[warrior.name] = warrior
            if warrior.faction not in self.factionsWarriors.keys():
                self.factionsWarriors[warrior.faction] = []   
            self.factionsWarriors[warrior.faction].append(warrior.name)
    
    
    def actualizeHP(self):
        if interaction.MOD == interaction.TERMINAL:
            for name in self.fightersNames.keys():
                someFighter = self.fightersNames[name]
                print(someFighter.name+" HP:"+str(someFighter.HP))
    
    def beginTurn(self):
        self.actualizeHP()
        for fighter in self.fighters:
            fighter.newTurn()    
        
    
    def checkValidity(self, fighter : fighter.CHARACTER, actions : List[Dict[str,Union[str,Tuple[int,int]]]], alliesName : List[str]):
        cost = 0
        for someAction in actions:
            if "Stoical_Defense" == someAction["name"] and len(actions) > 1:
                interaction.throwError("Can not use Stoical_defense and other action in same turn")
                return False
            if "useConsumable" == someAction["name"]:
                if fighter.getItemFromInventoryByName(someAction["target"]) == None:
                    interaction.throwError("Can not use item that fighter do not possess")
                    return False
            if ("Attack" in someAction["name"] or "Shot" in someAction["name"]):
                if "hand" not in someAction.keys():
                    interaction.throwError("error in game logic")
                    return False
                if someAction["hand"] == None:
                    interaction.throwError("Can not attack without weapon")
                    return False
                if someAction["hand"] == "left":
                    tool = fighter.leftTool
                    if tool == None:
                        interaction.throwError("no tool")
                        return False
                if someAction["hand"] == "right":
                    tool = fighter.rightTool
                
                if any(target == allyName for allyName in alliesName for target in someAction["targets"]):
                    interaction.throwError("Can not attack ally")
                    return False
                
            if "Attack" in someAction["name"]:
                if tool.name not in weapons.MELEE_WEAPONS:
                    interaction.throwError("Can not attack frontally with non melee weapon")
                    return False

            if someAction["name"] not in action.Action.ACTIONS_DICT.keys():
                interaction.throwError("Using an action "+someAction["name"]+" that does not exist")
                return False
            if someAction["name"] == "Equip":
                if not any(someAction["object"] == stuff.name for stuff in fighter.inventory):
                    interaction.throwError("Using an item that player do not possess")
                    return False
            if "Shot" in someAction["name"]:
                if tool.name not in weapons.RANGE_WEAPONS and tool.name not in weapons.THROWABLE:
                    interaction.throwError("Can not shot without range or throwable weapon")
                    return False
                if tool.name in weapons.THROWABLE and len(someAction["targets"] > 1):
                    interaction.throwError("Can not shot multi targets with throwable weapon")
                    return False
                
            cost += action.Action.ACTIONS_DICT[someAction["name"]].staminaCost
        if cost > fighter.stamina:
            interaction.throwError("Using too much stamina")
            return False
        return True
                
        
    def getPowerOfFaction(self, faction : str):
        power = 0
        for warriorName in self.factionsWarriors[faction]:
            warrior = self.fightersNames[warriorName]
            power += warrior.getEstimatedPower()
        return power
    
    def getWarriorsOfFaction(self, faction : str):
        warriors = []
        for warriorName in self.factionsWarriors[faction]:
            warrior = self.fightersNames[warriorName]
            warriors.append(warrior)
        return warriors

    def getEstimatedPowerOfFactions(self):
        power = {}
        for faction in self.factionsWarriors.keys():
            factionPower = self.getPowerOfFaction(faction)
            power[faction] = factionPower
        return power
    
    
    def prepareActions(self):
        for fighter in self.fighters:
            actionValidated = False
            while not actionValidated :
                interaction.showInformation("Turn of "+fighter.name+"\n")
                actions = fighter.setUpActions(self.fightersNames, self.getEstimatedPowerOfFactions(), {faction : self.getWarriorsOfFaction(faction) for faction in self.factionsWarriors.keys()})
                for someAction in actions:
                    someAction["name"]+=str(fighter.getStrLevelOfSkill(someAction["name"]))
                actionValidated = self.checkValidity(fighter, actions, self.factionsWarriors[fighter.faction])
            fighter.actions = actions
    
    def namesToCharacters(self, namesList : List[str]):
        fighters = []
        for name in namesList:
            if not any(name == dead.name for dead in self.defeatedWarriors):
                fighters.append(self.fightersNames[name])
        return fighters
    
    def killWarrior(self, fighter : fighter.CHARACTER):
        interaction.showInformation("Fighter "+fighter.name+" died")
        self.defeatedWarriors.append(fighter)
        self.factionsWarriors[fighter.faction].remove(fighter.name)
        self.fightersNames.pop(fighter.name,None)
        self.fighters.remove(fighter)
    
    def killByName(self, name: str):
        if name in self.fightersNames.keys():
            self.killWarrior(self.fightersNames[name])
    
    def executeActions(self):
        for fighter in self.fighters:
            if fighter.HP <= 0:
                self.killWarrior(fighter)
            else:    
                for actionDict in fighter.actions:
                    if "Defense" in actionDict["name"]:
                        action.Action.ACTIONS_DICT[actionDict["name"]].acts(fighter,None)
                        continue
        
        for fighter in rules.getTurnPriority(self.fighters):
                for actionDict in fighter.actions:
                    if "Movement" in actionDict["name"]:
                            action.Action.ACTIONS_DICT[actionDict["name"]].acts(fighter, actionDict["target"])
                    if "Attack" in actionDict["name"]:
                            action.Action.ACTIONS_DICT[actionDict["name"]].acts(fighter, self.namesToCharacters(actionDict["targets"]), actionDict["hand"])
                            continue
                    if "Equip" == actionDict["name"]:
                            action.Action.ACTIONS_DICT["Equip"].acts(fighter, fighter.getItemFromInventoryByName(actionDict["object"]), actionDict["hand"])
                            continue
                    if "Shot" in actionDict["name"]:
                        action.Action.ACTIONS_DICT[actionDict["name"]].acts(fighter, self.namesToCharacters(actionDict["targets"]), actionDict["hand"])
                        continue
                    if "useConsumable" == actionDict["name"]:
                        action.Action.ACTIONS_DICT["useConsumable"].acts(fighter, actionDict["target"])
                        continue
                    if "Melee_Combat" == actionDict["name"]:
                        action.Action.ACTIONS_DICT[actionDict["name"]].acts(fighter, self.namesToCharacters(actionDict["targets"]))
                        continue
    
                    
    def manualChanges(self):
        buf = ""
        while True:
            buf = input("Command of Game Master\n")
            if buf == "exit":
                break
            try:
                exec(buf)
            except Exception as e:
                print("something had gone wrong:")
                print(e)
    
    def hasBattleEnded(self):
        count = 0
        for faction in self.factionsWarriors.keys():
            if self.factionsWarriors[faction] != []:
                count += 1
            if count >= 2:
                return False
        assert count != 0 # means everyone died
        return True

    def checkForDeath(self, warriors: List[fighter.CHARACTER]):
        for fighter in warriors:
            if fighter.HP <= 0:
                self.killWarrior(fighter)
    
    def turn(self):
        self.beginTurn()
        self.prepareActions()
        if interaction.MOD == interaction.TERMINAL:
            self.manualChanges()
        self.executeActions()
        if interaction.MOD == interaction.TERMINAL:
            self.manualChanges()
        self.checkForDeath(self.fighters)
            
    
    def collectLoot(self):
        loot : List[Union[List[items.ITEM], int]] = [[],0] # (inventory, gold)
        for dead in self.defeatedWarriors:
            loot[0].extend(dead.inventory)
            if dead.money > 0:
                loot[1] += dead.money
        return loot
    
    def shareLoot(self, loot : Tuple[List[items.ITEM], int]):
        for item in loot[0]:
            given = False
            while not given:
                characterName = interaction.askFor("Who to give "+item.name+"\n")
                if characterName not in self.fightersNames.keys():
                    continue
                self.fightersNames[characterName].put_into_inventory(item)
                given = True
                
        while loot[1] != 0:
            characterName = interaction.askFor("Who to give gold\n")
            if characterName not in self.fightersNames.keys():
                continue
            amountStr = interaction.askFor("Remaining gold: "+str(loot[1])+", how much to give ?")
            if not amountStr.isdigit():
                interaction.throwError("That is not a number")
                continue
            amount = int(amountStr)
            if amount > loot[1]:
                continue
            else: 
                self.fightersNames[characterName].money += amount
                loot[1] -= amount
                
    
    def battle(self):
        self.checkForDeath(self.fighters)
        while not self.hasBattleEnded():
            self.turn()
        loot = self.collectLoot()
        self.shareLoot(loot)
        
        
        ## checking for upgrades ##
        for fighter in self.fighters:
            if isinstance(fighter, player.Player):
                for skill in fighter.actionCounter.keys():
                    lvSkill = defaultSkills.DEFAULT_SKILLS[skill][fighter.basicSkillsLevel[skill]]
                    while fighter.actionCounter[skill] > lvSkill["UpgradeExpCost"] and action.Action.ACTIONS_DICT[skill+fighter.getStrLevelOfSkill(skill)].upgrades != []:
                        upgradable = action.Action.ACTIONS_DICT[skill+fighter.getStrLevelOfSkill(skill)]
                        for upgradeSkill in upgradable.upgrades:
                            if not upgradeSkill.name.startswith(skill):
                                fighter.addSkill(upgradeSkill)
                            else:
                                fighter.upgradeSkill(skill)
                                rules.skillLevelUp(fighter,skill)
                fighter.saveFighter(fighter.name+".sav")

    @staticmethod             
    def instantiate_from_infos(players:List[player.Player], npc_fighters : List[Dict[str,str]]):
        warriors = [player for player in players]
        for npc_fighter in npc_fighters:
            warriors.append(fighter.CHARACTER.instantiate_from_class(**npc_fighter))
        return Battle(warriors)
    
