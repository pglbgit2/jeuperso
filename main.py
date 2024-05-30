import battle, player, rules, fighter, action, weapons, armors, consumable, defaultSkills


if __name__ == '__main__':
    action.setupActions()
    
    ## CREATE NEW PLAYER
    # newPlayer = player.Player(**player.Player.getCharacterInfos())
    # newPlayer.saveFighter(newPlayer.name+".sav")
    
    
    ## CREATE NEW FIGHTER
    # newFighter = fighter.CHARACTER(**fighter.CHARACTER.getCharacterInfos())
    # newFighter.saveFighter(newFighter.name+".sav")
    
    
    
    # billy = player.Player.retrieveFighter("billy.sav")
    # billy.inventory.append(consumable.Consumable.get_consumable("HEALTH_POTION"))
    
    
    #eloi = player.Player.retrieveFighter("Eloi.sav")
    
    pluton = player.Player.retrieveFighter("Pluton.sav")

    # pluton.saveFighter("Pluton.sav")
    
    pluton.printPlayerSheet()
    fabien = player.Player.retrieveFighter("Fabien.sav")
 
    #fabien.saveFighter("Fabien.sav")
    # #fabien.saveFighter("Fabien.sav")
    fabien.printPlayerSheet()
    
    # Sdrakeide = fighter.CHARACTER.retrieveFighter("Dorokaen.sav")
    # battle1 = battle.Battle([pluton, fabien])
    # battle1.battle()
    # Sdrakeide.saveFighter("Dorokaen.sav")
    
    # gothi = fighter.CHARACTER.retrieveFighter("Gothi.sav")
    # elowen = fighter.CHARACTER.retrieveFighter("Elowen.sav")
    # Wa_En = fighter.CHARACTER.retrieveFighter("Wa_Hen.sav")
    Eloi = player.Player.retrieveFighter("Eloi.sav")
    # Efraim = player.Player.retrieveFighter("Efraim.sav")    
    # bandit1 = fighter.CHARACTER.instantiate_from_class("THIEF","Mallory","Enemies","HUMAN")
    #bandit1.isControlledByGM = False
    #bandit2 = fighter.CHARACTER.instantiate_from_class("FOOTPAD","Mallory2","Enemies","HUMAN")
    #bandit2.isControlledByGM = False
    
    #bandit3 = fighter.CHARACTER.instantiate_from_class("THIEF","Mallory3","Enemies","HUMAN")
    #bandit3.isControlledByGM = False

    #bandit4 = fighter.CHARACTER.instantiate_from_class("FOOTPAD","Mallory4","Enemies","HUMAN")
    #bandit4.isControlledByGM = False

    #bandit5 = fighter.CHARACTER.instantiate_from_class("THIEF","Mallory5","Enemies","HUMAN")
    #bandit5.isControlledByGM = False

    # StreetsWatcher1 = fighter.CHARACTER.instantiate_from_class("MAGE","StreetWatcher1","Enemies","HUMAN")
    # StreetsWatcher2 = fighter.CHARACTER.instantiate_from_class("MAGE","StreetWatcher2","Enemies","HUMAN")
    # StreetsWatcher3 = fighter.CHARACTER.instantiate_from_class("MAGE","StreetWatcher3","Enemies","HUMAN")
    # Stilvor = fighter.CHARACTER.instantiate_from_class("MAGE","StreetWatcher4","Enemies","HUMAN")
    # battle1 = battle.Battle([ pluton, fabien, bandit2])
    # battle1.battle()
    
    
    
    
    # battle2 = battle.Battle.instantiate_from_infos([pluton, fabien],[{"characterClass":"DEFAULT_CLASS", "name":"spider", "faction":"Enemies", "race":"GIANT_SPIDER"}])
    # battle2.battle()
        
    
    ## TEST 1 ##
    # battle2 = battle.Battle.instantiate_from_infos([billy],[{"characterClass":"WARRIOR", "name":"war1", "faction":"Enemies", "race":"UNDEAD"}])
    # battle2.battle()
    
    ## TEST 2 ##
    
    # gard1 = fighter.CHARACTER.instantiate_from_class("CITY_GARD", "gard1", "Players","HUMAN")
    # gard2 = fighter.CHARACTER.instantiate_from_class("ARCHER", "gard2", "Players","HUMAN")
    
    # bandit = fighter.CHARACTER.instantiate_from_class("THIEF","Mallory","Enemies","HUMAN")
    # footpad = fighter.CHARACTER.instantiate_from_class("FOOTPAD", "Red", "Enemies","HUMAN")
    # bandit.isControlledByGM = False
    # footpad.isControlledByGM = False
    # gard1.isControlledByGM = False
    # gard2.isControlledByGM = False
    # battle1 = battle.Battle([bandit, billy, footpad])
    # battle1.battle()
    
     ## TEST 3 ##
    battle2 = battle.Battle.instantiate_from_infos([pluton, fabien, Eloi],[{"characterClass":"DEFAULT_CLASS", "name":"spider", "faction":"Enemies", "race":"GIANT_SPIDER"}])
    battle2.battle()
        
