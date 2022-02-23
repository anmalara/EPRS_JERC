from EPRBase import *

def EPRs_FastSim():
    university = 'FLORIDA-STATE'
    eprs = []
    eprs.append(EPRContainer(
        task       = 'JES -- MC Truth -- FastSim',
        user       = 'Purbita Rahman Prova',
        university = university,
        pledges    = 2,
        done       = 0,
        last_year  = 2,
        agreed     = False,
        approved   = False
        ))

    return eprs
