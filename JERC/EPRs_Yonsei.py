from EPRBase import *

def EPRs_Yonsei():
    university = 'YONSEI'
    eprs = []
    eprs.append(EPRContainer(
        task       = 'JER -- SF -- RC',
        user       = 'Seungkyu Ha',
        university = university,
        pledges    = 2,
        done       = 0,
        last_year  = 2,
        agreed     = True,
        approved   = False
        ))

    eprs.append(EPRContainer(
        task       = 'JER -- SF -- RC',
        user       = 'Guk Cho',
        university = university,
        pledges    = 2,
        done       = 0,
        last_year  = 1,
        agreed     = True,
        approved   = False
        ))

    return eprs
