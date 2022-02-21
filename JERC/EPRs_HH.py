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
        agreed     = False,
        approved   = False
        ))

    eprs.append(EPRContainer(
        task       = 'JER -- SF -- dijet',
        user       = 'Matthias Schroeder',
        university = university,
        pledges    = 1,
        done       = 0,
        last_year  = 2,
        agreed     = False,
        approved   = False
        ))

    eprs.append(EPRContainer(
        task       = 'JME Coffea',
        user       = 'Alexander Paasch',
        university = university,
        pledges    = 2,
        done       = 0,
        last_year  = 3,
        agreed     = False,
        approved   = False
        ))

    eprs.append(EPRContainer(
        task       = 'JME Coffea',
        user       = 'Matthias Schroeder',
        university = university,
        pledges    = 1,
        done       = 0,
        last_year  = 1,
        agreed     = False,
        approved   = False,
        note       = 'Used for coffea',
        ))

    eprs.append(EPRContainer(
        task       = 'JER -- SF -- dijet',
        user       = 'New student',
        university = university,
        pledges    = 3,
        done       = 0,
        last_year  = 0,
        agreed     = False,
        approved   = False,
        note       = 'Used for coffea',
        ))

    eprs.append(EPRContainer(
        task       = 'JME Coffea',
        user       = 'New student',
        university = university,
        pledges    = 3,
        done       = 0,
        last_year  = 0,
        agreed     = False,
        approved   = False,
        note       = 'Used for coffea',
        ))
    eprs.append(EPRContainer(
        task       = 'JER -- MC',
        user       = 'Patrick Connor',
        university = university,
        pledges    = 1,
        done       = 0,
        last_year  = 1,
        agreed     = False,
        approved   = False
        ))

    eprs.append(EPRContainer(
        task       = 'JER -- MC',
        user       = 'Polidamas Kosmoglou',
        university = 'Ioannina',
        pledges    = 2,
        done       = 0,
        last_year  = 1,
        agreed     = False,
        approved   = False
        ))

    eprs.append(EPRContainer(
        task       = 'JES -- L2 Res',
        user       = 'Mikel Mendizabal Morentin',
        university = 'DESY',
        pledges    = 0,
        done       = 0,
        last_year  = 2,
        agreed     = False,
        approved   = False
        ))

    eprs.append(EPRContainer(
        task       = 'JES -- L2 Res',
        user       = 'Jindrich Lidrych',
        university = '????',
        pledges    = 0,
        done       = 0,
        last_year  = 2,
        agreed     = False,
        approved   = False
        ))

    return eprs
