from EPRBase import *

def EPRs_HH():
    university = 'HAMBURG-UNIV'
    eprs = []
    eprs.append(EPRContainer(
        task       = 'JER -- SF -- dijet',
        user       = 'Alexander Paasch',
        university = university,
        pledges    = 2,
        done       = 0,
        last_year  = 3,
        agreed     = True,
        approved   = False
        ))

    eprs.append(EPRContainer(
        task       = 'JER -- SF -- dijet',
        user       = 'Matthias Schroeder',
        university = university,
        pledges    = 1,
        done       = 0,
        last_year  = 2,
        agreed     = True,
        approved   = False
        ))

    eprs.append(EPRContainer(
        task       = 'R&D',
        user       = 'Alexander Paasch',
        university = university,
        pledges    = 2,
        done       = 0,
        last_year  = 3,
        agreed     = True,
        approved   = False,
        note       = 'Taken from JES -- L2 Res in 2021',
        ))

    eprs.append(EPRContainer(
        task       = 'R&D',
        user       = 'Matthias Schroeder',
        university = university,
        pledges    = 1,
        done       = 0,
        last_year  = 1,
        agreed     = True,
        approved   = False,
        note       = 'Taken from JES -- L2 Res in 2021',
        ))

    eprs.append(EPRContainer(
        task       = 'JER -- SF -- dijet',
        user       = 'Yannick Fisher',
        university = university,
        pledges    = 2,
        done       = 0,
        last_year  = 0,
        agreed     = True,
        approved   = False,
        ))

    eprs.append(EPRContainer(
        task       = 'R&D',
        user       = 'Yannick Fisher',
        university = university,
        pledges    = 4,
        done       = 0,
        last_year  = 0,
        agreed     = True,
        approved   = False,
        ))

    eprs.append(EPRContainer(
        task       = 'JES -- MC Truth -- JER',
        user       = 'Patrick Connor',
        university = university,
        pledges    = 1,
        done       = 0,
        last_year  = 1,
        agreed     = True,
        approved   = False
        ))

    eprs.append(EPRContainer(
        task       = 'JES -- MC Truth -- JER',
        user       = 'Polidamas Kosmoglou',
        university = 'Ioannina',
        pledges    = 3,
        done       = 2,
        last_year  = 1,
        agreed     = True,
        approved   = False
        ))

    eprs.append(EPRContainer(
        task       = 'JES -- L2 Res',
        user       = 'Mikel Mendizabal Morentin',
        university = 'DESY',
        pledges    = 2,
        done       = 0,
        last_year  = 2,
        agreed     = True,
        approved   = False
        ))

    eprs.append(EPRContainer(
        task       = 'R&D',
        user       = 'Mikel Mendizabal Morentin',
        university = 'DESY',
        pledges    = 2,
        done       = 0,
        last_year  = 0,
        agreed     = True,
        approved   = False
        ))

    eprs.append(EPRContainer(
        task       = 'JES -- L2 Res',
        user       = 'Jindrich Lidrych',
        university = 'Northwestern',
        pledges    = 0,
        done       = 0,
        last_year  = 2,
        agreed     = True,
        approved   = False
        ))

    eprs.append(EPRContainer(
        task       = 'R&D',
        user       = 'Jindrich Lidrych',
        university = 'Northwestern',
        pledges    = 2,
        done       = 0,
        last_year  = 0,
        agreed     = True,
        approved   = False
        ))

    return eprs
