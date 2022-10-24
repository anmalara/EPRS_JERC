from EPRBase import *

def EPRs_Athens():
    university = 'ATHENS'
    eprs = []
    eprs.append(EPRContainer(
        task       = 'JES -- MC Truth -- L1L2L3',
        user       = 'Niki Saoulidou',
        university = university,
        pledges    = 4,
        done       = 0,
        last_year  = 4,
        agreed     = True,
        approved   = False
        ))

    eprs.append(EPRContainer(
        task       = 'JES -- MC Truth -- L1L2L3',
        user       = 'Ilias Zisopoulos',
        university = university,
        pledges    = 4,
        done       = 0,
        last_year  = 4,
        agreed     = True,
        approved   = False
        ))
    eprs.append(EPRContainer(
        task       = 'JES -- MC Truth -- L1L2L3',
        user       = 'Eirini Tziaferi',
        university = university,
        pledges    = 4,
        done       = 0,
        last_year  = 4,
        agreed     = True,
        approved   = False
        ))

    return eprs
