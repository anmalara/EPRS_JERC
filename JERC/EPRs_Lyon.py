from EPRBase import *

def EPRs_Lyon():
    university = 'LYON'
    eprs = []
    eprs.append(EPRContainer(
        task       = 'JES -- L3 Res -- gamma+jet',
        user       = 'Benjamin Blancon',
        university = university,
        pledges    = 3,
        done       = 0,
        last_year  = 3,
        agreed     = False,
        approved   = False,
        note       = 'Stephanie pledged in 21, not in 22',
        ))

    eprs.append(EPRContainer(
        task       = 'JES -- L3 Res -- gamma+jet',
        user       = 'Ji Eun',
        university = university,
        pledges    = 3,
        done       = 0,
        last_year  = 3,
        agreed     = False,
        approved   = False,
        note       = 'Stephanie pledged in 21, not in 22',
        ))

    return eprs
