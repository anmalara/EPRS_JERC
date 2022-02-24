from EPRBase import *

def EPRs_PFHadron():
    eprs = []
    eprs.append(EPRContainer(
        task       = 'PF Hadron Calibration',
        user       = 'Bhumika Kansal',
        university = 'PUNE-IISER',
        pledges    = 4,
        done       = 0,
        last_year  = 4,
        agreed     = False,
        approved   = False,
        note       = 'Possible to have them split',
        ))

    eprs.append(EPRContainer(
        task       = 'PF Hadron Calibration',
        user       = 'Juska Pekkanen',
        university = 'SUNY-BUFFALO',
        pledges    = 2,
        done       = 0,
        last_year  = 2,
        agreed     = False,
        approved   = False
        ))

    return eprs
