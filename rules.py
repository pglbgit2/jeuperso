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
    bodyBaseResistance = 0
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
        bodyBaseResistance = 3
    if defaultSkills.CD == skill:
        stamina_regenerationBonus += 0.2
    if defaultSkills.PS == skill:
        shotBonus += 0.02
    if defaultSkills.QS == skill:
        shotBonus += 0.02
    if defaultSkills.CS == skill:
        shotBonus += 0.02
    if any(skill == magicSkill for magicSkill in [defaultSkills.MS, defaultSkills.PF, defaultSkills.MAF, defaultSkills.WT, defaultSkills.EO, defaultSkills.ER, defaultSkills.FB, defaultSkills.FB, defaultSkills.FBa, defaultSkills.FS]):
        MaxMagicBonus += 0.1
        
    
    fighter.MaxHP += MaxHPBonus
    interaction.showInformation(fighter.name+" improve its MaxHP by "+str(MaxHPBonus)+", current MaxHP: "+str(fighter.MaxHP))
    fighter.stamina += staminaBonus
    interaction.showInformation(fighter.name+" improve its stamina by "+str(staminaBonus)+", current stamina: "+str(fighter.stamina))
    fighter.stamina_regeneration += stamina_regenerationBonus
    interaction.showInformation(fighter.name+" improve its stamina_regeneration by "+str(stamina_regenerationBonus)+", current MaxHP: "+str(fighter.stamina_regeneration))
    fighter.MaxMagic += MaxMagicBonus
    interaction.showInformation(fighter.name+" improve its MaxMagicBonus by "+str(MaxMagicBonus)+", current MaxHP: "+str(fighter.MaxMagic))
    for part in ["head", "legs", "torso"]:
        fighter.bodyBaseResistance[part] += bodyBaseResistance
    interaction.showInformation(fighter.name+" improve its body Defense by "+str(bodyBaseResistance))
    fighter.shotBonus += shotBonus
    interaction.showInformation(fighter.name+" improve its shotBonus by "+str(shotBonus)+", current shotBonus: "+str(fighter.shotBonus))




def getTurnPriority(units: List[fighter.CHARACTER], mod=PRIORITY):
    if mod == PRIORITY_BY_SPEED:
        return sorted(units, key=lambda x: x.get_speed(), reverse=True)
    
    if mod == PRIORITY_BY_INITIATIVE:
        return sorted(units, key= lambda x: x.getInitiative(), reverse=True)
    
    return units

