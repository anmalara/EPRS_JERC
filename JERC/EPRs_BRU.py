from EPRBase import *

def EPRs_BRU():
    university = 'BRUXELLES-ULB'
    eprs = []
    eprs.append(EPRContainer(
        task       = 'L3 Conveners',
        user       = 'Andrea Malara',
        university = university,
        pledges    = 2,
        done       = 0,
        last_year  = 2,
        agreed     = True,
        approved   = False,
        note       = 'Effective only '+str(round(1./3,2))+'. The rest for the previous convener.'
        ))

    eprs.append(EPRContainer(
        task       = 'R&D',
        user       = 'Andrea Malara',
        university = university,
        pledges    = 1,
        done       = 0,
        last_year  = 0,
        agreed     = True,
        approved   = False
        ))

    eprs.append(EPRContainer(
        task       = 'JER -- SF -- dijet',
        user       = 'Andrea Malara',
        university = university,
        pledges    = 2,
        done       = 0,
        last_year  = 3,
        agreed     = True,
        approved   = False
        ))

    eprs.append(EPRContainer(
        task       = 'JER -- SF -- zjet',
        user       = 'Laurent Thomas',
        university = university,
        pledges    = 0,
        done       = 0,
        last_year  = 2,
        agreed     = True,
        approved   = False
        ))

    eprs.append(EPRContainer(
        task       = 'JER -- SF -- zjet',
        user       = 'Soumya Dansana',
        university = university,
        pledges    = 3,
        done       = 0,
        last_year  = 0,
        agreed     = True,
        approved   = False,
        note       = 'Pledge in JES -- L1 Res for 2021',
        ))

    eprs.append(EPRContainer(
        task       = 'JES -- L1 Res',
        user       = 'Soumya Dansana',
        university = university,
        pledges    = 0,
        done       = 0,
        last_year  = 3,
        agreed     = True,
        approved   = False
        ))


    return eprs
