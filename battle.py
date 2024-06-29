import fighter, rules, action, player, interaction, items, readline, weapons, defaultSkills, actionsTypes
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
        self.ground = []
        for warrior in fighters:
            self.fightersNames[warrior.name] = warrior
            if warrior.faction not in self.factionsWarriors.keys():
                self.factionsWarriors[warrior.faction] = []   
            self.factionsWarriors[warrior.faction].append(warrior.name)
    
    
    def actualizeHP(self):
        if interaction.MOD == interaction.TERMINAL:
            for name in self.fightersNames.keys():
                someFighter = self.fightersNames[name]
                print(someFighter.name+" HP:"+str(someFighter.HP)+" Magic:"+str(someFighter.magic)+" left hand: "+ ("Nothing" if someFighter.leftTool == None else str(someFighter.leftTool.name))+" right hand:"+ ("Nothing" if someFighter.rightTool == None else str(someFighter.rightTool.name)))
    
    def beginTurn(self):
        for fighter in self.fighters:
            fighter.newTurn() 
        self.actualizeHP()
   
        
    
    def checkValidity(self, fighter : fighter.CHARACTER, actions : List[Dict[str,Union[str,Tuple[int,int]]]], alliesName : List[str]):
        cost = 0
        manaCost = 0
        for someAction in actions:
            actionName = someAction["name"]
            if "Stoical_Defense" == actionName and len(actions) > 1:
                interaction.throwError("Can not use Stoical_defense and other action in same turn")
                return False
            if "useConsumable" == actionName:
                if fighter.getItemFromInventoryByName(someAction["otherInfos"]["Equipment"]) == None:
                    interaction.throwError("Can not use item that fighter do not possess")
                    return False
            if ("Attack" in actionName or "Shot" in actionName):
                if "hand" not in someAction["otherInfos"].keys():
                    interaction.throwError("error in game logic")
                    return False
                hand = someAction["otherInfos"]["hand"]
                if hand == None:
                    interaction.throwError("Can not attack without weapon")
                    return False
                if hand == "left":
                    tool = fighter.leftTool
                    if tool == None:
                        interaction.throwError("no tool")
                        return False
                if hand == "right":
                    tool = fighter.rightTool
                    if tool == None:
                        interaction.throwError("no tool")
                        return False
            if "Quick_Attack" in actionName and tool in weapons.HEAVY:
                interaction.throwError("Can not quick attack with heavy weapon")

                return False
            if any(actionName in NoFriendlyFireAction for NoFriendlyFireAction in actionsTypes.NotFriendlyAggressiveActions):
                if any(target == allyName for allyName in alliesName for target in someAction["targets"]):
                    interaction.throwError("Can not attack ally")
                    return False
                
            if "Attack" in actionName:
                if tool.name not in weapons.MELEE_WEAPONS:
                    interaction.throwError("Can not attack frontally with non melee weapon")
                    return False

            if actionName not in action.Action.ACTIONS_DICT.keys():
                interaction.throwError("Using an action "+actionName+" that does not exist")
                return False
            if actionName == "Equip":
                if not any(someAction["object"] == stuff.name for stuff in fighter.inventory):
                    interaction.throwError("Using an item that player do not possess")
                    return False
            if "Shot" in actionName:
                if tool.name not in weapons.RANGE_WEAPONS and tool.name not in weapons.THROWABLE:
                    interaction.throwError("Can not shot without range or throwable weapon")
                    return False
                if tool.name in weapons.THROWABLE and len(someAction["targets"] > 1):
                    interaction.throwError("Can not shot multi targets with throwable weapon")
                    return False
            if any(actionName.startswith(manaCostingAction) for manaCostingAction in actionsTypes.ManaCostingActions):
                manaCost += action.Action.ACTIONS_DICT[actionName].manaCost
                
            if actionName.startswith("Protection_Field") or actionName.startswith("Minor_Shield"):
                if not all(any(target == allyName for allyName in alliesName) for target in someAction["targets"]):
                    interaction.throwError("Can not protect other than ally")
                    return False
                
            cost += action.Action.ACTIONS_DICT[actionName].staminaCost
        if cost > fighter.stamina:
            interaction.throwError("Using too much stamina")
            return False
        if manaCost > fighter.magic:
            interaction.throwError("Using too much mana")
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
    
    def prepareOneCharacterAction(self, fighterName:str):
        if fighterName in self.fightersNames.keys():
            chosenFighter = self.fightersNames[fighterName]
            actionValidated = False
            while not actionValidated :
                interaction.showInformation("Choosed "+chosenFighter.name+"\n")
                actions = chosenFighter.setUpActions(self.fightersNames, self.getEstimatedPowerOfFactions(), {faction : self.getWarriorsOfFaction(faction) for faction in self.factionsWarriors.keys()})
                for someAction in actions:
                    someAction["name"]+=str(chosenFighter.getStrLevelOfSkill(someAction["name"]))
                actionValidated = self.checkValidity(chosenFighter, actions, self.factionsWarriors[chosenFighter.faction])
            chosenFighter.actions = actions
            
    def executeOneCharacterAction(self, fighterName:str):
        if fighterName in self.fightersNames.keys():
            chosenFighter = self.fightersNames[fighterName]
            for actionDict in chosenFighter.actions:
                actionName = actionDict["name"]
                if "Defense" in actionName:
                    action.Action.ACTIONS_DICT[actionName].acts(chosenFighter,None,None)
                    return
                if "Protection_Field" in actionName or "Minor_Shield" in actionName:
                    action.Action.ACTIONS_DICT[actionName].acts(chosenFighter, self.namesToCharacters(actionDict["targets"]), None)
                    return
                if "Minor_Aggressive_Flux" in actionName or "Wrath_Torrent" in actionName:
                    action.Action.ACTIONS_DICT[actionName].acts(chosenFighter,None, None)
                        
                        
    def namesToCharacters(self, namesList : List[str]):
        fighters = []
        for name in namesList:
            if not any(name == dead.name for dead in self.defeatedWarriors):
                fighters.append(self.fightersNames[name])
          
        return fighters
    
    def killWarrior(self, warrior : fighter.CHARACTER):
        interaction.showInformation("Fighter "+warrior.name+" died")
        if not isinstance(warrior, player.Player):
            self.defeatedWarriors.append(warrior)
        else: fighter.saveFighter(fighter.name+".sav")
        self.factionsWarriors[warrior.faction].remove(warrior.name)
        self.fightersNames.pop(warrior.name,None)
        self.fighters.remove(warrior)
    
    def killByName(self, name: str):
        if name in self.fightersNames.keys():
            self.killWarrior(self.fightersNames[name])
        
    def doPassiveAction(self, fighter:fighter.CHARACTER):
        for actionDict in fighter.actions:
            actionName = actionDict["name"]
            if "Defense" in actionName:
                action.Action.ACTIONS_DICT[actionName].acts(fighter,None,None)
                continue
            if "Protection_Field" in actionName or "Minor_Shield" in actionName:
                action.Action.ACTIONS_DICT[actionName].acts(fighter, self.namesToCharacters(actionDict["targets"]), None)
                continue
            if "Minor_Aggressive_Flux" in actionName or "Wrath_Torrent" in actionName:
                action.Action.ACTIONS_DICT[actionName].acts(fighter,None, None)
                continue
            if "Unshakable_Fortress" in actionName or "Solid_Skin" in actionName:
                action.Action.ACTIONS_DICT[actionName].acts(fighter,None, actionDict["otherInfos"])

    
    
    def doActiveActions(self, fighter:fighter.CHARACTER):
        for actionDict in fighter.actions:
            actionName = actionDict["name"]
            if "Movement" in actionName:
                action.Action.ACTIONS_DICT[actionName].acts(fighter, actionDict["target"], actionDict["otherInfos"])
                continue
            if "Attack" in actionName or "Melee_Combat" in actionName:
                action.Action.ACTIONS_DICT[actionName].acts(fighter, self.namesToCharacters(actionDict["targets"]), actionDict["otherInfos"])
                continue
            if "Equip" == actionName:
                action.Action.ACTIONS_DICT["Equip"].acts(fighter, None, {"item" : fighter.getItemFromInventoryByName(actionDict["object"]), "bodyPart" : actionDict["bodyPart"]})
                continue
            if "Shot" in actionName:
                throw = action.Action.ACTIONS_DICT[actionName].acts(fighter, self.namesToCharacters(actionDict["targets"]), actionDict["otherInfos"])
                if throw != None:
                    self.ground.append(throw)
                continue
            if "useConsumable" == actionName:
                action.Action.ACTIONS_DICT["useConsumable"].acts(fighter, None, actionDict["otherInfos"])
                continue
            if "Energy_Blade" == actionName:
                action.Action.ACTIONS_DICT[actionName].acts(fighter,None,None)
                continue
            if any(actionName.startswith(EAA) for EAA in actionsTypes.EnergyAggressiveActions):
                action.Action.ACTIONS_DICT[actionName].acts(fighter,self.namesToCharacters(actionDict["targets"]), actionDict["otherInfos"])
    
    def executeActions(self):
        for fighter in self.fighters:
            if fighter.HP <= 0:
                self.killWarrior(fighter)
            else:    
                self.doPassiveAction(fighter)
        
        for fighter in rules.getTurnPriority(self.fighters):
                if fighter.HP <= 0:
                    self.killWarrior(fighter)
                    continue
                interaction.showInformation("Turn of "+fighter.name)
                if interaction.MOD == interaction.TERMINAL:
                    self.manualChanges()
                self.doActiveActions(fighter)
                    
    
                    
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
            print(fighter.name)
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
                self.fightersNames[characterName].money += int(amount)
                loot[1] -= int(amount)
                
    
    def battle(self):
        self.checkForDeath(self.fighters)
        while not self.hasBattleEnded():
            self.turn()
        for fighter in self.fighters:
            if isinstance(fighter, player.Player):
                fighter.saveFighter(fighter.name+".sav")

        loot = self.collectLoot()
        self.shareLoot(loot)
        
        
        ## checking for upgrades ##
        for fighter in self.fighters:
            if isinstance(fighter, player.Player):
                fighter.saveFighter(fighter.name+".sav")

                for skill in fighter.actionCounter.keys():
                    if skill not in defaultSkills.NOT_UPGRADABLE and skill in defaultSkills.UPGRADABLE.keys(): 
                        lvSkill = defaultSkills.UPGRADABLE[skill][fighter.basicSkillsLevel[skill]]
                        while fighter.actionCounter[skill] > defaultSkills.UPGRADABLE[skill][fighter.basicSkillsLevel[skill]]["UpgradeExpCost"] and action.Action.ACTIONS_DICT[skill+fighter.getStrLevelOfSkill(skill)].upgrades != []:
                            upgradable = action.Action.ACTIONS_DICT[skill+fighter.getStrLevelOfSkill(skill)]
                            for upgradeSkill in upgradable.upgrades:
                                if not upgradeSkill.name.startswith(skill):
                                    fighter.addSkill(upgradeSkill)
                                else:
                                    hasLevelUp = fighter.upgradeSkill(skill)
                                    if not hasLevelUp:
                                        fighter.actionCounter[skill] = 0 # to avoid leveling up this skill each turn after maxed out
                                    rules.skillLevelUp(fighter,skill)
                fighter.saveFighter(fighter.name+".sav")

    @staticmethod             
    def instantiate_from_infos(players:List[player.Player], npc_fighters : List[Dict[str,str]]):
        warriors = [player for player in players]
        for npc_fighter in npc_fighters:
            warriors.append(fighter.CHARACTER.instantiate_from_class(**npc_fighter))
        return Battle(warriors)
    
