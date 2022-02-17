from EPRBase import *

def EPRs_Buffalo():
    university = 'SUNY-BUFFALO'
    eprs = []
    eprs.append(EPRContainer(
        task       = 'JES -- L1 Res',
        user       = 'Ia Iashvili',
        university = university,
        pledges    = 0,
        done       = 0,
        last_year  = 3,
        agreed     = False,
        approved   = False
        ))

    eprs.append(EPRContainer(
        task       = 'JER -- MC',
        user       = 'Ia Iashvili',
        university = university,
        pledges    = 0,
        done       = 0,
        last_year  = 1,
        agreed     = False,
        approved   = False
        ))

    eprs.append(EPRContainer(
        task       = 'JES -- L1 Res',
        user       = 'Hirak Bandyopadhyay',
        university = university,
        pledges    = 0,
        done       = 0,
        last_year  = 5,
        agreed     = False,
        approved   = False
        ))

    eprs.append(EPRContainer(
        task       = 'JER -- MC',
        user       = 'Hirak Bandyopadhyay',
        university = university,
        pledges    = 0,
        done       = 0,
        last_year  = 2,
        agreed     = False,
        approved   = False
        ))

    return eprs
