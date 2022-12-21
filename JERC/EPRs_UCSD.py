from EPRBase import *

def EPRs_UCSD():
    university = 'UCSD'
    eprs = []
    eprs.append(EPRContainer(
        task       = 'JES -- Flavor and composition',
        user       = 'Stephane Cooperstein',
        university = university,
        pledges    = 1,
        done       = 0,
        last_year  = 0,
        agreed     = False,
        approved   = False
        ))

    return eprs
