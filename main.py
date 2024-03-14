import battle, player, fighter


if __name__ == '__main__':
    gard1 = fighter.CHARACTER.instantiate_from_class("CITY_GARD", "gard1", "Heroes","HUMAN")
    gard2 = fighter.CHARACTER.instantiate_from_class("ARCHER", "gard2", "Heroes","HUMAN")
    bandit = fighter.CHARACTER.instantiate_from_class("THIEF","Mallory","Bandits","HUMAN")
    footpad = fighter.CHARACTER.instantiate_from_class("FOOTPAD", "Red", "Bandits","HUMAN")
    bandit.isControlledByGM = False
    footpad.isControlledByGM = False
    battle1 = battle.Battle([gard1,bandit,gard2,footpad])
    battle1.battle()
        
