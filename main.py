import battle, player, fighter, action, consumable


if __name__ == '__main__':
    action.setupActions()
    
    billy = player.Player.retrieveFighter("billy.sav")
    billy.inventory.append(consumable.Consumable.get_consumable("HEALTH_POTION"))
    
    
    ## TEST 1 ##
    # battle2 = battle.Battle.instantiate_from_infos([billy],[{"characterClass":"WARRIOR", "name":"war1", "faction":"Bandits", "race":"UNDEAD"}])
    # battle2.battle()
    
    ## TEST 2 ##
    
    # gard1 = fighter.CHARACTER.instantiate_from_class("CITY_GARD", "gard1", "Heroes","HUMAN")
    # gard2 = fighter.CHARACTER.instantiate_from_class("ARCHER", "gard2", "Heroes","HUMAN")
    # bandit = fighter.CHARACTER.instantiate_from_class("THIEF","Mallory","Bandits","HUMAN")
    # footpad = fighter.CHARACTER.instantiate_from_class("FOOTPAD", "Red", "Bandits","HUMAN")
    # bandit.isControlledByGM = False
    # footpad.isControlledByGM = False
    # gard1.isControlledByGM = False
    # gard2.isControlledByGM = False
    # battle1 = battle.Battle([bandit, billy, footpad])
    # battle1.battle()
    
     ## TEST 1 ##
    battle2 = battle.Battle.instantiate_from_infos([billy],[{"characterClass":"DEFAULT_CLASS", "name":"spider", "faction":"Bandits", "race":"GIANT_SPIDER"}])
    battle2.battle()
        
