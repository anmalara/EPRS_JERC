from EPRBase import *

def EPRs_Buffalo():
    university = 'SUNY-BUFFALO'
    eprs = []
    eprs.append(EPRContainer(
        task       = 'JES -- L1 Res',
        user       = 'Ia Iashvili',
        university = university,
        pledges    = 1,
        done       = 0,
        last_year  = 3,
        agreed     = True,
        approved   = False
        ))

    eprs.append(EPRContainer(
        task       = 'JES -- MC Truth -- JER',
        user       = 'Ia Iashvili',
        university = university,
        pledges    = 1.5,
        done       = 0,
        last_year  = 1,
        agreed     = True,
        approved   = False
        ))

    eprs.append(EPRContainer(
        task       = 'JES -- L1 Res',
        user       = 'Hirak Bandyopadhyay',
        university = university,
        pledges    = 1,
        done       = 0,
        last_year  = 5,
        agreed     = True,
        approved   = False
        ))

    eprs.append(EPRContainer(
        task       = 'JES -- MC Truth -- JER',
        user       = 'Hirak Bandyopadhyay',
        university = university,
        pledges    = 3.5,
        done       = 0,
        last_year  = 2,
        agreed     = True,
        approved   = False
        ))

    eprs.append(EPRContainer(
        task       = 'R&D',
        user       = 'Garvita Agarwal',
        university = university,
        pledges    = 2,
        done       = 0,
        last_year  = 0,
        agreed     = True,
        approved   = False
        ))

    eprs.append(EPRContainer(
        task       = 'R&D',
        user       = 'Salvatore Rappoccio',
        university = university,
        pledges    = 1,
        done       = 0,
        last_year  = 0,
        agreed     = False,
        approved   = False
        ))

    eprs.append(EPRContainer(
        task       = 'R&D',
        user       = 'Margaret Morris',
        university = university,
        pledges    = 2,
        done       = 0,
        last_year  = 0,
        agreed     = False,
        approved   = False
        ))

    eprs.append(EPRContainer(
        task       = 'R&D',
        user       = 'AC Williams',
        university = university,
        pledges    = 2,
        done       = 0,
        last_year  = 0,
        agreed     = False,
        approved   = False
        ))

    return eprs
