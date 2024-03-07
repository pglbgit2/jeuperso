import fighter, rules, action, player, interaction, items
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
        map(lambda x: x.newTurn(),self.fighters)    
        
    
    def checkValidity(self, fighter : fighter.CHARACTER, actions : List[Dict[str,Union[str,Tuple[int,int]]]], alliesName : List[str]):
        for someAction in actions:
            if "Stoical_Defense" == someAction and len(actions) > 1:
                interaction.throwError("Can not use Stoical_defense and other action in same turn")
                return False
            if "Attack" in someAction["name"] and any(someAction["target"] == allyName for allyName in alliesName):
                interaction.throwError("Can not attack ally")
                return False
            if someAction["name"] not in action.Action.ACTIONS_DICT.keys():
                interaction.throwError("Using an action "+someAction["name"]+" that does not exist")
                return False
            if someAction["name"] == "Equip":
                if not any(someAction["object"] == stuff for stuff in fighter.inventory):
                    interaction.throwError("Using an item that player do not possess")
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
                actions = fighter.setUpActions(self.fightersNames, self.getEstimatedPowerOfFactions(), [self.getWarriorsOfFaction(faction) for faction in self.factionsWarriors.keys()])
                for someAction in actions:
                    someAction["name"]+=str(fighter.getStrLevelOfSkill(someAction["name"]))
                actionValidated = not isinstance(fighter, player.Player) or self.checkValidity(fighter, actions, self.factionsWarriors[fighter.faction])
            fighter.actions = actions
    
    def namesToCharacters(self, namesList : List[str]):
        fighters = []
        for name in namesList:
            fighters.append(self.fightersNames[name])
        return fighters
    
    def killWarrior(self, fighter : fighter.CHARACTER):
        self.defeatedWarriors.append(fighter)
        self.factionsWarriors[fighter.faction].remove(fighter.name)
        self.fightersNames.pop(fighter.name,None)
    
    def executeActions(self):
        for fighter in rules.getTurnPriority(self.fighters):
            if fighter.HP <= 0:
                self.killWarrior(fighter)
            else:    
                for actionDict in fighter.actions:
                    if "Attack" in actionDict["name"]:
                        action.Action.ACTIONS_DICT[actionDict["name"]].acts(fighter, self.namesToCharacters(actionDict["targets"]), actionDict["hand"])
                        continue
                    if "Equip" == actionDict["name"]:
                        action.Action.ACTIONS_DICT["Equip"].acts(fighter, fighter.getItemFromInventoryByName(actionDict["name"]), actionDict["hand"])
                        continue
                    if "Defense" in actionDict["name"]:
                        action.Action.ACTIONS_DICT[actionDict["name"]].acts(fighter,None)
                        continue
                    if "Movement" in actionDict["name"]:
                        action.Action.ACTIONS_DICT[actionDict["name"]].acts(fighter, actionDict["target"])
    
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
                
    def turn(self):
        self.beginTurn()
        self.prepareActions()
        self.executeActions()
        if interaction.MOD == interaction.TERMINAL:
            self.manualChanges()
            
    
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
                characterName = interaction.askFor("Who to give "+item.name)
                if characterName not in self.fightersNames.keys():
                    continue
                self.fightersNames[characterName].put_into_inventory(item)
                
        while loot[1] != 0:
            characterName = interaction.askFor("Who to give gold")
            if characterName not in self.fightersNames.keys():
                continue
            amountStr = interaction.askFor("Remaining gold: "+loot[1]+", how much to give ?")
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
        while not self.hasBattleEnded():
            self.turn()
        loot = self.collectLoot()
        self.shareLoot(loot)
        