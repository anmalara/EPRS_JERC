from JERC.EPRs_Athens import *
from JERC.EPRs_BRU import *
from JERC.EPRs_Buffalo import *
from JERC.EPRs_Calo import *
from JERC.EPRs_FastSim import *
from JERC.EPRs_HIP import *
from JERC.EPRs_HH import *
from JERC.EPRs_Lyon import *
from JERC.EPRs_KIT import *
from JERC.EPRs_PFHadron import *
from JERC.EPRs_Yonsei import *


def EPRs_JERC():
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
