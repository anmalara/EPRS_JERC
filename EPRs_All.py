from EPRs_Athens import *
from EPRs_BRU import *
from EPRs_Buffalo import *
from EPRs_Calo import *
from EPRs_FastSim import *
from EPRs_HIP import *
from EPRs_HH import *
from EPRs_Lyon import *
from EPRs_KIT import *
from EPRs_PFHadron import *
from EPRs_Yonsei import *


def EPRs_All():
    eprs = []
    eprs.extend(EPRs_Athens())
    eprs.extend(EPRs_BRU())
    eprs.extend(EPRs_Buffalo())
    eprs.extend(EPRs_Calo())
    eprs.extend(EPRs_FastSim())
    eprs.extend(EPRs_HIP())
    eprs.extend(EPRs_HH())
    eprs.extend(EPRs_Lyon())
    eprs.extend(EPRs_KIT())
    eprs.extend(EPRs_PFHadron())
    eprs.extend(EPRs_Yonsei())

    return eprs
