from EPRBase import *

def EPRs_Riga():
    university = 'RIGA'
    eprs = []
    eprs.append(EPRContainer(
        task       = 'JES -- Flavor and composition',
        user       = 'Markus Seidel',
        university = university,
        pledges    = 1,
        done       = 0,
        last_year  = 0,
        agreed     = True,
        approved   = False,
        note       = '',
        ))

    eprs.append(EPRContainer(
        task       = 'JES -- Flavor and composition',
        user       = 'Andris Potrebko',
        university = university,
        pledges    = 2,
        done       = 0,
        last_year  = 0,
        agreed     = True,
        approved   = False,
        note       = '',
        ))

    return eprs
