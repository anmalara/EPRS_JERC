#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
from prettytable import PrettyTable
from EPRs_JERC import *


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--expand', '-e', action='store_true', default=False, dest='expand', help='Show all info')
    args = parser.parse_args()
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
    
    table_totals = PrettyTable(infos)
    for info in infos:
            table_totals.align[info] = 'l'

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
        table_totals.add_row(summary)
        if args.expand:
            print(table,'\n')

    summary = ['' for x in infos]
    summary[infos.index('task')] = cyan('Total')
    for tot in totals:
        summary[infos.index(tot)] = cyan(totals[tot])
    table_totals.add_row(summary)
    print(table_totals,'\n')
   


if __name__ == '__main__':
    main()
