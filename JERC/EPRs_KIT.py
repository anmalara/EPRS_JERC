from EPRBase import *

def EPRs_KIT():
    university = 'KARLSRUHE-IEKP'
    eprs = []
    eprs.append(EPRContainer(
        task       = 'JES -- L3 Res -- Z+jet',
        user       = 'Robin Hofsaess',
        university = university,
        pledges    = 2,
        done       = 0,
        last_year  = 4,
        agreed     = False,
        approved   = False
        ))

    eprs.append(EPRContainer(
        task       = 'JES -- L3 Res -- Z+jet',
        user       = 'Ralf Florian Von Cube',
        university = university,
        pledges    = 0,
        done       = 0,
        last_year  = 2,
        agreed     = False,
        approved   = False
        ))

    eprs.append(EPRContainer(
        task       = 'JES -- L3 Res -- Z+jet',
        user       = 'Maximilian Horzela',
        university = university,
        pledges    = 0,
        done       = 0,
        last_year  = 2,
        agreed     = False,
        approved   = False
        ))

    return eprs
