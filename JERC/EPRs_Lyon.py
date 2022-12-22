from EPRBase import *

def EPRs_Lyon():
    university = 'LYON'
    eprs = []

    eprs.append(EPRContainer(
        task       = 'JES -- L3 Res -- gamma+jet',
        user       = 'Benjamin Blancon',
        university = university,
        pledges    = 1,
        done       = 0,
        last_year  = 3,
        agreed     = True,
        approved   = False,
        note       = 'Reduced 6->4.5: less work',
        ))

    eprs.append(EPRContainer(
        task       = 'JES -- L3 Res -- gamma+jet',
        user       = 'Benjamin Blancon',
        university = university,
        pledges    = 1.5,
        done       = 0,
        last_year  = 0,
        agreed     = True,
        approved   = False,
        ))

    eprs.append(EPRContainer(
        task       = 'JES -- L3 Res -- gamma+jet',
        user       = 'Ji Eun Choi',
        university = university,
        pledges    = 2,
        done       = 0,
        last_year  = 0,
        agreed     = True,
        approved   = False,
        ))

    return eprs
