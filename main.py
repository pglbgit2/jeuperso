import battle, player, rules, fighter, action, weapons, armors, consumable, defaultSkills


if __name__ == '__main__':
    action.setupActions()
    
    ## CREATE NEW PLAYER
    # newPlayer = player.Player(**player.Player.getCharacterInfos())
    # newPlayer.saveFighter(newPlayer.name+".sav")
    
    
    ## CREATE NEW FIGHTER
    # newFighter = fighter.CHARACTER(**fighter.CHARACTER.getCharacterInfos())
    # newFighter.saveFighter(newFighter.name+".sav")
    
    
    
    billy = player.Player.retrieveFighter("billy.sav")
    billy.inventory.append(consumable.Consumable.get_consumable("HEALTH_POTION"))
    billy.inventory.append(consumable.Consumable.get_consumable("ANTIDOTE"))
    billy.inventory.append(consumable.Consumable.get_consumable("POISON"))

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
    # Eloi.saveFighter("Eloi.sav")
    # Efraim = player.Player.retrieveFighter("Efraim.sav")    
    #bandit1 = fighter.CHARACTER.instantiate_from_class("THIEF","Mallory","Enemies","HUMAN")
    #bandit1.isControlledByGM = False
    snake1 = fighter.CHARACTER.instantiate_from_class("DEFAULT_CLASS", "snake1", "Enemies", "SNAKE")
    bat1 = fighter.CHARACTER.instantiate_from_class("DEFAULT_CLASS", "snake1", "Enemies", "BAT")
    spider1 = fighter.CHARACTER.instantiate_from_class("DEFAULT_CLASS", "snake1", "Enemies", "GIANT_SPIDER")
    battle1 = battle.Battle([ billy, snake1])
    battle1.battle()
    # StreetsWatcher1 = fighter.CHARACTER.instantiate_from_class("MAGE","StreetWatcher1","Enemies","HUMAN")
   
    # Stilvor = fighter.CHARACTER.instantiate_from_class("MAGE","StreetWatcher4","Enemies","HUMAN")
    battle1 = battle.Battle([ pluton, fabien, snake1])
    battle1.battle()
    
        
    
