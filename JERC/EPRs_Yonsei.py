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
        agreed     = False,
        approved   = False
        ))

    eprs.append(EPRContainer(
        task       = 'JER -- SF -- RC',
        user       = 'Guk Cho',
        university = university,
        pledges    = 3,
        done       = 0,
        last_year  = 1,
        agreed     = False,
        approved   = False
        ))

    return eprs
