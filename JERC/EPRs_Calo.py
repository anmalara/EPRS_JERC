from EPRBase import *

def EPRs_Calo():
    university = 'MOSCOW-MSU'
    eprs = []
    eprs.append(EPRContainer(
        task       = 'JES -- MC Truth -- Calo/JPT',
        user       = 'Olga Kodolova',
        university = university,
        pledges    = 1,
        done       = 0,
        last_year  = 1,
        agreed     = True,
        approved   = False
        ))

    return eprs
