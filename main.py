import battle, player, fighter


if __name__ == '__main__':
    gard1 = fighter.CHARACTER.instantiate_from_race("CITY_GARD", "gard1", "Heroes")
    bandit = fighter.CHARACTER.instantiate_from_race("THIEF","Mallory","Bandits")
    battle1 = battle.Battle([gard1,bandit])
    battle1.battle()
        