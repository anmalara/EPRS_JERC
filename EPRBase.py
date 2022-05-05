from collections import OrderedDict

def modify_printed_string(type,string): return "%s%s\033[0m"%(type,string)

def red(string):     return modify_printed_string('\x1b[0;31m',string)
def green(string):   return modify_printed_string('\x1b[0;32m',string)
def yellow(string):  return modify_printed_string('\x1b[0;33m',string)
def blue(string):    return modify_printed_string('\x1b[0;34m',string)
def magenta(string): return modify_printed_string('\x1b[0;35m',string)
def cyan(string):    return modify_printed_string('\x1b[0;36m',string)
def bold(string):    return modify_printed_string('\033[1m',string)

def TaskColor(task):
    color = None
    if task=='JES -- MC Truth -- L1L2L3':     color = red
    if task=='JES -- MC Truth -- Calo/JPT':   color = magenta
    if task=='JES -- MC Truth -- FastSim':    color = magenta
    if task=='JES -- MC Truth -- JER':        color = green
    if task=='JES -- L1 Res':                 color = blue
    if task=='JES -- L2 Res':                 color = blue
    if task=='JES -- L3 Res -- gamma+jet':    color = blue
    if task=='JES -- L3 Res -- Z+jet':        color = blue
    if task=='JES -- L3 Res -- multijet':     color = blue
    if task=='JES -- L3 Res -- Wqq':          color = blue
    if task=='JES -- Flavor and composition': color = blue
    if task=='JES -- Global fit':             color = blue
    if task=='JER -- SF -- RC':               color = green
    if task=='JER -- SF -- dijet':            color = green
    if task=='JER -- SF -- zjet':             color = green
    if task=='PF Hadron Calibration':         color = magenta
    if task=='R&D':                           color = cyan
    if task=='L3 Conveners':                  color = cyan
    if color==None:
        print('Missing task:',task)
    return color

def EPR_infos():
    return ['task','user','university','pledges','last_year','agreed','done', 'approved', 'note']

def EPR_tasks():
    return [
        'JES -- MC Truth -- L1L2L3',
        'JES -- MC Truth -- JER',
        'JES -- MC Truth -- FastSim',
        'JES -- MC Truth -- Calo/JPT',
        'JES -- L1 Res',
        'JES -- L2 Res',
        'JES -- L3 Res -- gamma+jet',
        'JES -- L3 Res -- Z+jet',
        'JES -- L3 Res -- multijet',
        'JES -- L3 Res -- Wqq',
        'JES -- Flavor and composition',
        'JES -- Global fit',
        'JER -- SF -- RC',
        'JER -- SF -- dijet',
        'JER -- SF -- zjet',
        'PF Hadron Calibration',
        'R&D',
        'L3 Conveners',
        ]

def EPR_categories():
    return {
        'JES -- MC Truth': 24,
        'JES -- L1 Res': 2,
        'JES -- L2 Res': 8,
        'JES -- L3 Res -- gamma+jet': 6,
        'JES -- L3 Res -- Z+jet': 6,
        'JES -- L3 Res -- multijet': 6,
        'JES -- L3 Res -- Wqq': 4,
        'JES -- Flavor and composition': 8,
        'JES -- Global fit': 8,
        'JER -- SF': 17,
        'PF Hadron Calibration': 6,
        'L3 Conveners': 4,
        'R&D': 18,
        }
def EPR_expected_per_category(category):
    return EPR_categories()[category]


class EPRContainer():
    def __init__(self, **kwargs):
        self.infos = {**kwargs}
        if not 'note' in self.infos:
            self.infos['note'] = ''

    def get_value(self, key):
        return self.infos[key]

    def get_row(self):
        color = TaskColor(self.get_value('task'))
        return list(color(self.get_value(x)) for x in EPR_infos())
