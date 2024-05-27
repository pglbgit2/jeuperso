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
MC = "Melee_Combat"
MS = "Minor_Shield"
PF = "Protection_Field"
MAF = "Minor_Aggressive_Flux"
WT = "Wrath_Torrent"
EO = "EnergyOrb"
ER = "EnergyRay"
FB = "FireBreath"
FBa = "FireBall"
FS = "FireStorm"
NOT_UPGRADABLE = [E, uC, MC]


DEFAULT_SKILLS = [QM, CM, SM, BA, QA, CA, LD, SD, CD, E, uC, MC, PS, QS, CS ]

UPGRADABLE = { 
    FB : {
        1 : {"ManaCost" : 2, "UpgradeExpCost" : 15, "damage" : 4, "dodge_alteration" : 0, "damageType" : "fire"},
        2 : {"ManaCost" : 3, "UpgradeExpCost" : 30, "damage" : 5, "dodge_alteration" : 0, "damageType" : "fire"},
        3 : {"ManaCost" : 4, "UpgradeExpCost" : 45, "damage" : 6, "dodge_alteration" : 0, "damageType" : "fire"},
    },
    FBa : {
        1 : {"ManaCost" : 6, "UpgradeExpCost" : 15, "damage" : 10, "dodge_alteration" : 0, "damageType" : "fire"},
        2 : {"ManaCost" : 7, "UpgradeExpCost" : 30, "damage" : 11, "dodge_alteration" : 0, "damageType" : "fire"},
        3 : {"ManaCost" : 8, "UpgradeExpCost" : 45, "damage" : 12, "dodge_alteration" : 0, "damageType" : "fire"},
    },
    FS: {
        1 : {"ManaCost" : 10, "UpgradeExpCost" : 15, "damage" : 15, "dodge_alteration" : 0, "damageType" : "fire"},
        2 : {"ManaCost" : 11, "UpgradeExpCost" : 30, "damage" : 18, "dodge_alteration" : 0, "damageType" : "fire"},
        3 : {"ManaCost" : 12, "UpgradeExpCost" : 45, "damage" : 20, "dodge_alteration" : 0, "damageType" : "fire"},
    }
    ,
    MS : {
        1 : {"ManaCost" : 3, "UpgradeExpCost" : 10, "protection" : 3, "dodge_alteration" : 0},
        2 : {"ManaCost" : 3, "UpgradeExpCost" : 25, "protection" : 5, "dodge_alteration" : 0},
        3 : {"ManaCost" : 3, "UpgradeExpCost" : 25, "protection" : 8, "dodge_alteration" : 0},

    },
    PF:{
        1 : {"ManaCost" : 6, "UpgradeExpCost" : 10, "protection" : 8, "dodge_alteration" : 0},
        2 : {"ManaCost" : 6, "UpgradeExpCost" : 25, "protection" : 12, "dodge_alteration" : 0},
        3 : {"ManaCost" : 6, "UpgradeExpCost" : 30, "protection" : 15, "dodge_alteration" : 0},
    },
    EO : {
         1 : {"ManaCost" : 8, "UpgradeExpCost" : 10, "damage" : 10, "dodge_alteration" : 0, "damageType" : "impact"},
        2 : {"ManaCost" : 9, "UpgradeExpCost" : 25, "damage" : 14, "dodge_alteration" : 0, "damageType" : "impact"},
        3 : {"ManaCost" : 10, "UpgradeExpCost" : 30, "damage" : 19, "dodge_alteration" : 0, "damageType" : "impact"},
    },
    ER : {
        1 : {"ManaCost" : 6, "UpgradeExpCost" : 10, "damage" : 4, "dodge_alteration" : 0, "damageType" : "arcane"},
        2 : {"ManaCost" : 6, "UpgradeExpCost" : 25, "damage" : 6, "dodge_alteration" : 0, "damageType" : "arcane"},
        3 : {"ManaCost" : 7, "UpgradeExpCost" : 30, "damage" : 8, "dodge_alteration" : 0, "damageType" : "arcane"},
    },
    MAF:{
        1 : {"ManaCost" : 3, "UpgradeExpCost" : 10, "damageBoost" : 2, "dodge_alteration" : 0},
        2 : {"ManaCost" : 3, "UpgradeExpCost" : 25, "damageBoost" : 4, "dodge_alteration" : 0},
        3 : {"ManaCost" : 4, "UpgradeExpCost" : 40, "damageBoost" : 6, "dodge_alteration" : 0},

    },
    WT:{
      1 : {"ManaCost" : 6, "UpgradeExpCost" : 10, "damageBoost" : 6, "dodge_alteration" : 0},
      2 : {"ManaCost" : 6, "UpgradeExpCost" : 25, "damageBoost" : 8, "dodge_alteration" : 0},
      3 : {"ManaCost" : 6, "UpgradeExpCost" : 40, "damageBoost" : 10, "dodge_alteration" : 0},
    }, 
    QM : {
        1 : {"StaminaCost" : 3, "UpgradeExpCost" : 10, "speed" : 5, "dodge_alteration" : -0.25},
        2 : {"StaminaCost" : 3, "UpgradeExpCost" : 25, "speed" : 8, "dodge_alteration" : -0.25},
        3 : {"StaminaCost" : 3, "UpgradeExpCost" : 45, "speed" : 10, "dodge_alteration" : -0.25},
        4 : {"StaminaCost" : 3, "UpgradeExpCost" : 65, "speed" : 12, "dodge_alteration" : -0.25}
    },
    CM : {
        1 : {"StaminaCost" : 2, "UpgradeExpCost" : 10, "speed" : 3, "dodge_alteration" : 0},
        2 : {"StaminaCost" : 2, "UpgradeExpCost" : 20, "speed" : 4, "dodge_alteration" : 0},
        3 : {"StaminaCost" : 2, "UpgradeExpCost" : 35, "speed" : 5, "dodge_alteration" : 0},
        4 : {"StaminaCost" : 2, "UpgradeExpCost" : 50, "speed" : 6, "dodge_alteration" : 0},
        5 : {"StaminaCost" : 2, "UpgradeExpCost" : 65, "speed" : 7, "dodge_alteration" : 0}
    },
    SM : {
        1 : {"StaminaCost" : 1, "UpgradeExpCost" : 10, "speed" : 1, "dodge_alteration" : 0.15},
        2 : {"StaminaCost" : 1, "UpgradeExpCost" : 20, "speed" : 1, "dodge_alteration" : 0.20},
        3 : {"StaminaCost" : 1, "UpgradeExpCost" : 30, "speed" : 1, "dodge_alteration" : 0.25},
        4 : {"StaminaCost" : 1, "UpgradeExpCost" : 40, "speed" : 1, "dodge_alteration" : 0.30},
        5 : {"StaminaCost" : 1, "UpgradeExpCost" : 50, "speed" : 1, "dodge_alteration" : 0.35}
    },
    QA : {
        1 : {"StaminaCost" : 3, "UpgradeExpCost" : 10,  "dodge_alteration" : 0,"damageFactor" : 0.5},
        2 : {"StaminaCost" : 3, "UpgradeExpCost" : 20, "dodge_alteration" : 0,"damageFactor" : 0.6},
        3 : {"StaminaCost" : 3, "UpgradeExpCost" : 30, "dodge_alteration" : 0,"damageFactor" : 0.7},
        4 : {"StaminaCost" : 3, "UpgradeExpCost" : 40, "dodge_alteration" : 0,"damageFactor" : 0.75},
        5 : {"StaminaCost" : 3, "UpgradeExpCost" : 50, "dodge_alteration" : 0,"damageFactor" : 0.8},
        6 : {"StaminaCost" : 3, "UpgradeExpCost" : 60, "dodge_alteration" : 0,"damageFactor" : 0.85}

    },
    CA : {
        1 : {"StaminaCost" : 2, "UpgradeExpCost" : 10,  "dodge_alteration" : 0,"damageFactor" : 1},
        2 : {"StaminaCost" : 2, "UpgradeExpCost" : 20, "dodge_alteration" : 0,"damageFactor" : 1.15},
        3 : {"StaminaCost" : 1, "UpgradeExpCost" : 30, "dodge_alteration" : 0,"damageFactor" : 1.25},
        4 : {"StaminaCost" : 1, "UpgradeExpCost" : 45, "dodge_alteration" : 0,"damageFactor" : 1.40},
        5 : {"StaminaCost" : 1, "UpgradeExpCost" : 60, "dodge_alteration" : 0,"damageFactor" : 1.50},
        6 : {"StaminaCost" : 1, "UpgradeExpCost" : 75, "dodge_alteration" : 0,"damageFactor" : 1.60},
        7 : {"StaminaCost" : 1, "UpgradeExpCost" : 90, "dodge_alteration" : 0,"damageFactor" : 1.70}
    },
    LD : {
        1 : {"StaminaCost" : 1, "UpgradeExpCost" : 10,  "dodge_alteration" : 0,"defensePoints" : 1},
        2 : {"StaminaCost" : 1, "UpgradeExpCost" : 20, "dodge_alteration" : 0,"defensePoints" : 2},
        3 : {"StaminaCost" : 1, "UpgradeExpCost" : 30, "dodge_alteration" : 0,"defensePoints" : 3},
        4 : {"StaminaCost" : 1, "UpgradeExpCost" : 45, "dodge_alteration" : 0,"defensePoints" : 4},
        5 : {"StaminaCost" : 1, "UpgradeExpCost" : 60, "dodge_alteration" : 0,"defensePoints" : 5},
        6 : {"StaminaCost" : 1, "UpgradeExpCost" : 75, "dodge_alteration" : 0,"defensePoints" : 6}
    },
    SD : {
        1 : {"StaminaCost" : 5, "UpgradeExpCost" : 10,  "dodge_alteration" : -100,"defensePoints" : -3},
        2 : {"StaminaCost" : 5, "UpgradeExpCost" : 20, "dodge_alteration" : -100,"defensePoints" : -5},
        3 : {"StaminaCost" : 5, "UpgradeExpCost" : 30, "dodge_alteration" : -100,"defensePoints" : -8},
        4 : {"StaminaCost" : 5, "UpgradeExpCost" : 40, "dodge_alteration" : -100,"defensePoints" : -10}
    },
    CD : {
        1 : {"StaminaCost" : 2, "UpgradeExpCost" : 10,  "dodge_alteration" : 0,"defensePoints" : 4},
        2 : {"StaminaCost" : 3, "UpgradeExpCost" : 20, "dodge_alteration" : 0,"defensePoints" : 6},
        3 : {"StaminaCost" : 3, "UpgradeExpCost" : 30, "dodge_alteration" : 0,"defensePoints" : 8},
        4 : {"StaminaCost" : 3, "UpgradeExpCost" : 45, "dodge_alteration" : 0.05,"defensePoints" : 9},
        5 : {"StaminaCost" : 3, "UpgradeExpCost" : 60, "dodge_alteration" : 0.10,"defensePoints" : 10},
        6 : {"StaminaCost" : 3, "UpgradeExpCost" : 75, "dodge_alteration" : 0.15,"defensePoints" : 11}
    },
    BA : {
        1 : {"StaminaCost" : 4, "UpgradeExpCost" : 10,  "dodge_alteration" : -100,"damageFactor" : 2.25},
        2 : {"StaminaCost" : 4, "UpgradeExpCost" : 20, "dodge_alteration" : -100,"damageFactor" : 2.5},
        3 : {"StaminaCost" : 4, "UpgradeExpCost" : 30, "dodge_alteration" : -100, "damageFactor" : 3},
        4 : {"StaminaCost" : 5, "UpgradeExpCost" : 40, "dodge_alteration" : -100, "damageFactor" : 4}, 
        5 : {"StaminaCost" : 6, "UpgradeExpCost" : 50, "dodge_alteration" : -100, "damageFactor" : 5},
        6 : {"StaminaCost" : 7, "UpgradeExpCost" : 60, "dodge_alteration" : -100, "damageFactor" : 6}  
    },
    PS : {
        1 : {"StaminaCost" : 4, "UpgradeExpCost" : 10,  "dodge_alteration" : 0,"accuracy" : 0.6},
        2 : {"StaminaCost" : 3, "UpgradeExpCost" : 20, "dodge_alteration" : 0,"accuracy" : 0.65},
        3 : {"StaminaCost" : 3, "UpgradeExpCost" : 30, "dodge_alteration" : 0,"accuracy" : 0.70},
        4 : {"StaminaCost" : 3, "UpgradeExpCost" : 45, "dodge_alteration" : 0,"accuracy" : 0.75},
        5 : {"StaminaCost" : 3, "UpgradeExpCost" : 60, "dodge_alteration" : 0,"accuracy" : 0.85}
    },
    QS : {
        1 : {"StaminaCost" : 2, "UpgradeExpCost" : 10,  "dodge_alteration" : 0,"accuracy" : 0.2},
        2 : {"StaminaCost" : 3, "UpgradeExpCost" : 20, "dodge_alteration" : 0.1,"accuracy" : 0.25},
        3 : {"StaminaCost" : 3, "UpgradeExpCost" : 30, "dodge_alteration" : 0.15,"accuracy" : 0.3},
        4 : {"StaminaCost" : 3, "UpgradeExpCost" : 45, "dodge_alteration" : 0.20,"accuracy" : 0.4},
        5 : {"StaminaCost" : 3, "UpgradeExpCost" : 60, "dodge_alteration" : 0.25,"accuracy" : 0.5}
    },
    CS : {
        1 : {"StaminaCost" : 3, "UpgradeExpCost" : 10,  "dodge_alteration" : 0,"accuracy" : 0.4},
        2 : {"StaminaCost" : 3, "UpgradeExpCost" : 20, "dodge_alteration" : 0,"accuracy" : 0.45},
        3 : {"StaminaCost" : 3, "UpgradeExpCost" : 30, "dodge_alteration" : 0,"accuracy" : 0.5},
        4 : {"StaminaCost" : 3, "UpgradeExpCost" : 45, "dodge_alteration" : 0,"accuracy" : 0.55},
        5 : {"StaminaCost" : 3, "UpgradeExpCost" : 60, "dodge_alteration" : 0,"accuracy" : 0.6},
    }, 
   
    
}

