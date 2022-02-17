#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from prettytable import PrettyTable
from EPRs_JERC import *


def main():
    filter_by = None

    # filter_by = ('task','JER -- SF -- dijet')

    EPRS = []
    EPRS.extend(EPRs_JERC())
    for epr in EPRS:
        if not epr.get_value('task') in EPR_tasks():
            raise Exception('EPR task not known!!')

    infos = EPR_infos()
    tasks = EPR_tasks()
    totals = { 'pledges': 0, 'done': 0, 'last_year': 0}

    for task in tasks:
        table = PrettyTable(infos)
        for info in infos:
            table.align[info] = 'l'

        totals_epr = { 'pledges': 0, 'done': 0, 'last_year': 0}
        for epr in EPRS:
            if epr.get_value('task')!=task: continue
            table.add_row(epr.get_row())
            for x in totals_epr:
                totals_epr[x] += epr.get_value(x)

        summary = ['' for x in infos]
        summary[infos.index('task')] = yellow('Total')
        for name, tot in totals_epr.items():
            totals[name]+=tot
            summary[infos.index(name)] = yellow(tot)

        table.add_row(summary)
        print(table,'\n')

    for tot in totals:
        print(cyan(tot+' = '+str(totals[tot])))


if __name__ == '__main__':
    main()
