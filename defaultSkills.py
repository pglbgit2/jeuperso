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

DEFAULT_SKILLS = [QM, CM, SM, BA, QA, CA, LD, SD, CD, E, PS, QS, CS]
NOT_UPGRADABLE = [E]

DEFAULT_SKILLS_COST = { 
    QM : 3,
    CM : 2,
    SM : 1,
    QA : 3,
    CA : 2,
    LD : 1,
    SD : 5,
    CD : 2,
    BA : 4,
    PS : 4,
    QS : 2,
    CS : 3
}

BA_EXP_UPGRADE_BY_LV = 0.3