import battle, player, fighter, action


if __name__ == '__main__':
    action.setupActions()
    gard1 = fighter.CHARACTER.instantiate_from_class("CITY_GARD", "gard1", "Heroes","HUMAN")
    gard2 = fighter.CHARACTER.instantiate_from_class("ARCHER", "gard2", "Heroes","HUMAN")
    billy = player.Player.retrieveFighter("billy.sav")
    bandit = fighter.CHARACTER.instantiate_from_class("THIEF","Mallory","Bandits","HUMAN")
    footpad = fighter.CHARACTER.instantiate_from_class("FOOTPAD", "Red", "Bandits","HUMAN")
    bandit.isControlledByGM = False
    footpad.isControlledByGM = False
    gard1.isControlledByGM = False
    gard2.isControlledByGM = False
    battle1 = battle.Battle([bandit, billy, footpad])
    battle1.battle()
        
