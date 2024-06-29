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
    # billy.inventory.append(consumable.Consumable.get_consumable("ANTIDOTE"))
    # billy.inventory.append(consumable.Consumable.get_consumable("POISON"))

    pluton = player.Player.retrieveFighter("Pluton.sav")
    # pluton.saveFighter("Pluton.sav")
    
    # pluton.printPlayerSheet()
    fabien = player.Player.retrieveFighter("Fabien.sav")
    #fabien.saveFighter("Fabien.sav")
    # #fabien.saveFighter("Fabien.sav")
    # fabien.printPlayerSheet()
    
    # Sdrakeide = fighter.CHARACTER.retrieveFighter("Dorokaen.sav")
    # battle1 = battle.Battle([pluton, fabien])
    # battle1.battle()
    # Sdrakeide.saveFighter("Dorokaen.sav")
    
    # gothi = fighter.CHARACTER.retrieveFighter("Gothi.sav")
    # elowen = fighter.CHARACTER.retrieveFighter("Elowen.sav")
    # Wa_En = fighter.CHARACTER.retrieveFighter("Wa_Hen.sav")
    Eloi = player.Player.retrieveFighter("Eloi.sav")
    Cryftoren = player.Player.retrieveFighter("Cryftoren.sav")
   
    Efraim = player.Player.retrieveFighter("Efraim.sav")
    #bandit1 = fighter.CHARACTER.instantiate_from_class("THIEF","Mallory","Enemies","HUMAN")
    #bandit1.isControlledByGM = False
    snake1 = fighter.CHARACTER.instantiate_from_class("DEFAULT_CLASS", "snake1", "Enemies", "SNAKE")
    bat1 = fighter.CHARACTER.instantiate_from_class("DEFAULT_CLASS", "bat1", "Enemies", "BAT")
    spider1 = fighter.CHARACTER.instantiate_from_class("DEFAULT_CLASS", "spider1", "Enemies", "GIANT_SPIDER")
    
    goblin1 = fighter.CHARACTER.instantiate_from_class("THIEF","goblin1","Enemies","GOBLIN")
    goblin1.isControlledByGM = False
    goblin2 = fighter.CHARACTER.instantiate_from_class("THIEF","goblin2","Enemies","GOBLIN")
    goblin2.isControlledByGM = False

    # goblin3 = fighter.CHARACTER.instantiate_from_class("THIEF","goblin3","Enemies","GOBLIN")
    # goblin4 = fighter.CHARACTER.instantiate_from_class("THIEF","goblin4","Enemies","GOBLIN")
    # goblin5 = fighter.CHARACTER.instantiate_from_class("THIEF","goblin5","Enemies","GOBLIN")
    # goblin6 = fighter.CHARACTER.instantiate_from_class("THIEF","goblin6","Enemies","GOBLIN")
    # goblin7 = fighter.CHARACTER.instantiate_from_class("THIEF","goblin7","Enemies","GOBLIN")
    # goblin8 = fighter.CHARACTER.instantiate_from_class("THIEF","goblin8","Enemies","GOBLIN")
    # goblin9 = fighter.CHARACTER.instantiate_from_class("THIEF","goblin9","Enemies","GOBLIN")
    # goblin10 = fighter.CHARACTER.instantiate_from_class("THIEF","goblin10","Enemies","GOBLIN")

    # StreetsWatcher1 = fighter.CHARACTER.instantiate_from_class("MAGE","StreetWatcher1","Enemies","HUMAN")
   
    # Stilvor = fighter.CHARACTER.instantiate_from_class("MAGE","StreetWatcher4","Enemies","HUMAN")
    battle1 = battle.Battle([ pluton, fabien, Eloi, Cryftoren, goblin1, goblin2])
    battle1.battle()
    
    
    # battle2 = battle.Battle.instantiate_from_infos([pluton, fabien], [{"characterClass":"DEFAULT_CLASS", "name":"spider2", "faction": "Enemies", "race":"GIANT_SPIDER"}])
    # battle2.battle()
        
    
