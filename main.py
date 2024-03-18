import battle, player, fighter, action


if __name__ == '__main__':
    action.setupActions()
    gard1 = fighter.CHARACTER.instantiate_from_class("CITY_GARD", "gard1", "Heroes","HUMAN")
    gard2 = fighter.CHARACTER.instantiate_from_class("ARCHER", "gard2", "Heroes","HUMAN")
    billy = player.Player.retrieveFighter("billy.sav")
    billy.actionCounter["Brutal_Attack"] = 30
    bandit = fighter.CHARACTER.instantiate_from_class("THIEF","Mallory","Bandits","HUMAN")
    footpad = fighter.CHARACTER.instantiate_from_class("FOOTPAD", "Red", "Bandits","HUMAN")
    bandit.HP=0
    bandit.isControlledByGM = False
    footpad.isControlledByGM = False
    footpad.HP=0
    battle1 = battle.Battle([gard1,bandit, billy, gard2,footpad])
    battle1.battle()
    print(billy.basicSkillsLevel["Brutal_Attack"])
        
