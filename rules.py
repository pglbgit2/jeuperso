from typing import List
import fighter, interaction
import defaultSkills

PRIORITY_BY_SPEED = 0
PRIORITY_BY_INITIATIVE = 1
PRIORITY = PRIORITY_BY_INITIATIVE


def skillLevelUp(fighter : fighter.CHARACTER, skill : str):
    MaxHPBonus = 0.25
    staminaBonus = 0.25
    stamina_regenerationBonus = 0.1
    MaxMagicBonus = 0.05
    defenseByTurnBonus = 0
    shotBonus = 0
    if defaultSkills.CM == skill:
        MaxHPBonus += 0.25
    if defaultSkills.QM == skill:
        staminaBonus += 0.25
    if defaultSkills.SM == skill:
        MaxHPBonus += 0.25
    if defaultSkills.BA == skill:
        staminaBonus += 0.25
    if defaultSkills.QA == skill:
        staminaBonus += 0.25
    if defaultSkills.CA == skill:
        staminaBonus += 0.25
    if defaultSkills.LD == skill:
        MaxHPBonus += 0.25
    if defaultSkills.SD == skill:
        defenseByTurnBonus = 1
    if defaultSkills.CD == skill:
        stamina_regenerationBonus += 0.2
    if defaultSkills.PS == skill:
        shotBonus += 0.05
    if defaultSkills.QS == skill:
        shotBonus += 0.05
    if defaultSkills.CS == skill:
        shotBonus += 0.05
    
    fighter.MaxHp += MaxHPBonus
    interaction.showInformation(fighter.name+" improve its MaxHP by "+str(MaxHPBonus)+", current MaxHP: "+str(fighter.MaxHP))
    fighter.stamina += staminaBonus
    interaction.showInformation(fighter.name+" improve its stamina by "+str(staminaBonus)+", current stamina: "+str(fighter.stamina))
    fighter.stamina_regeneration += stamina_regenerationBonus
    interaction.showInformation(fighter.name+" improve its stamina_regeneration by "+str(stamina_regenerationBonus)+", current MaxHP: "+str(fighter.stamina_regeneration))
    fighter.MaxMagic += MaxMagicBonus
    interaction.showInformation(fighter.name+" improve its MaxMagicBonus by "+str(MaxMagicBonus)+", current MaxHP: "+str(fighter.MaxMagic))
    fighter.defenseByTurn += defenseByTurnBonus
    interaction.showInformation(fighter.name+" improve its defenseByTurn by "+str(defenseByTurnBonus)+", current MaxHP: "+str(fighter.defenseByTurn))
    fighter.shotBonus += shotBonus
    interaction.showInformation(fighter.name+" improve its shotBonus by "+str(shotBonus)+", current shotBonus: "+str(fighter.shotBonus))




def getTurnPriority(units: List[fighter.CHARACTER], mod=PRIORITY):
    if mod == PRIORITY_BY_SPEED:
        return sorted(units, key=lambda x: x.get_speed(), reverse=True)
    
    if mod == PRIORITY_BY_INITIATIVE:
        return sorted(units, key= lambda x: x.getInitiative(), reverse=True)
    
    return units

