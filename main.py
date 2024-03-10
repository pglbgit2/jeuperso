import battle, player, fighter


if __name__ == '__main__':
    gard1 = fighter.CHARACTER.instantiate_from_race("CITY_GARD", "gard1", "Heroes")
    gard2 = fighter.CHARACTER.instantiate_from_race("ARCHER", "gard2", "Heroes")
    bandit = fighter.CHARACTER.instantiate_from_race("THIEF","Mallory","Bandits")
    footpad = fighter.CHARACTER.instantiate_from_race("FOOTPAD", "Red", "Bandits")
    bandit.isControlledByGM = False
    footpad.isControlledByGM = False
    battle1 = battle.Battle([gard1,bandit,gard2,footpad])
    battle1.battle()
        
