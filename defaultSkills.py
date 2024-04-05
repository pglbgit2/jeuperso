QM = "Quick_Movement"
CM = "Classic_Movement"
SM = "Slow_Movement"
BA = "Brutal_Attack"
QA = "Quick_Attack"
CA = "Classic_Attack"
LD = "Light_Defense"
SD = "Stoical_Defense"
CD = "Classic_Defense"
E = "Equip"
PS = "Precise_Shot"
QS = "Quick_Shot"
CS = "Classic_Shot"
uC = "useConsumable"

NOT_UPGRADABLE = [E, uC]

DEFAULT_SKILLS = { 
    QM : {
        1 : {"StaminaCost" : 3, "UpgradeExpCost" : 10, "speed" : 5, "dodge_alteration" : -0.15},
        2 : {"StaminaCost" : 3, "UpgradeExpCost" : 25, "speed" : 8, "dodge_alteration" : -0.20}
    },
    CM : {
        1 : {"StaminaCost" : 2, "UpgradeExpCost" : 10, "speed" : 3, "dodge_alteration" : 0},
        2 : {"StaminaCost" : 2, "UpgradeExpCost" : 20, "speed" : 4, "dodge_alteration" : 0}
    },
    SM : {
        1 : {"StaminaCost" : 1, "UpgradeExpCost" : 10, "speed" : 1, "dodge_alteration" : 0.15},
        2 : {"StaminaCost" : 1, "UpgradeExpCost" : 20, "speed" : 1, "dodge_alteration" : 0.20}
    },
    QA : {
        1 : {"StaminaCost" : 3, "UpgradeExpCost" : 10,  "dodge_alteration" : 0,"damageFactor" : 0.5},
        2 : {"StaminaCost" : 3, "UpgradeExpCost" : 20, "dodge_alteration" : 0,"damageFactor" : 0.5}
    },
    CA : {
        1 : {"StaminaCost" : 2, "UpgradeExpCost" : 10,  "dodge_alteration" : 0,"damageFactor" : 1},
        2 : {"StaminaCost" : 2, "UpgradeExpCost" : 20, "dodge_alteration" : 0,"damageFactor" : 1}
    },
    LD : {
        1 : {"StaminaCost" : 1, "UpgradeExpCost" : 10,  "dodge_alteration" : 0,"defensePoints" : 1},
        2 : {"StaminaCost" : 3, "UpgradeExpCost" : 20, "dodge_alteration" : 0,"defensePoints" : 1}
    },
    SD : {
        1 : {"StaminaCost" : 5, "UpgradeExpCost" : 10,  "dodge_alteration" : -100,"defensePoints" : -3},
        2 : {"StaminaCost" : 5, "UpgradeExpCost" : 20, "dodge_alteration" : -100,"defensePoints" : -5}
    },
    CD : {
        1 : {"StaminaCost" : 2, "UpgradeExpCost" : 10,  "dodge_alteration" : 0,"defensePoints" : 4},
        2 : {"StaminaCost" : 3, "UpgradeExpCost" : 20, "dodge_alteration" : 0,"defensePoints" : 5}
    },
    BA : {
        1 : {"StaminaCost" : 4, "UpgradeExpCost" : 10,  "dodge_alteration" : -100,"damageFactor" : 2.25},
        2 : {"StaminaCost" : 4, "UpgradeExpCost" : 20, "dodge_alteration" : -100,"damageFactor" : 2.5},
        3 : {"StaminaCost" : 4, "UpgradeExpCost" : 30, "dodge_alteration" : -100, "damageFactor" : 2.75} 
    },
    PS : {
        1 : {"StaminaCost" : 4, "UpgradeExpCost" : 10,  "dodge_alteration" : 0,"accuracy" : 0.6},
        2 : {"StaminaCost" : 3, "UpgradeExpCost" : 20, "dodge_alteration" : 0,"accuracy" : 0.65}
    },
    QS : {
        1 : {"StaminaCost" : 2, "UpgradeExpCost" : 10,  "dodge_alteration" : 0,"accuracy" : 0.2},
        2 : {"StaminaCost" : 3, "UpgradeExpCost" : 20, "dodge_alteration" : 0,"accuracy" : 0.25}
    },
    CS : {
        1 : {"StaminaCost" : 3, "UpgradeExpCost" : 10,  "dodge_alteration" : 0,"accuracy" : 0.4},
        2 : {"StaminaCost" : 3, "UpgradeExpCost" : 20, "dodge_alteration" : 0,"accuracy" : 0.45}
    }
}

