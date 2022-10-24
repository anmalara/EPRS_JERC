#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
from copy import deepcopy
from prettytable import PrettyTable
from EPRs_JERC import *

def CreateTable(infos):
    table = PrettyTable(infos)
    for info in infos:
        table.align[info] = 'l'
    return table

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--expand', '-e', action='store_true', default=False, dest='expand', help='Show all info')
    args = parser.parse_args()

    infos = EPR_infos()
    tasks = EPR_tasks()
    totals = { 'pledges': 0, 'done': 0, 'last_year': 0, 'note':0, 'agreed': True, 'approved': True}

    EPRS = []
    EPRS.extend(EPRs_JERC())
    for epr in EPRS:
        if not epr.get_value('task') in tasks:
            raise Exception('EPR task not known!!')

    table_totals = CreateTable(infos)
    previous_category = None
    for task in tasks:
        total_epr_per_task = { 'pledges': 0, 'done': 0, 'last_year': 0, 'agreed': True, 'approved': True}
        table = CreateTable(infos)
        for epr in EPRS:
            if epr.get_value('task')!=task: continue
            table.add_row(epr.get_row())
            for x in total_epr_per_task:
                val = epr.get_value(x)
                if x =='agreed' or x=='approved':
                    total_epr_per_task[x] *= val
                else:
                    total_epr_per_task[x] += val

        summary_per_task = ['' for x in infos]
        summary_per_task[infos.index('task')] = yellow('Total')
        for name, tot in total_epr_per_task.items():
            if name =='agreed' or name=='approved':
                totals[name] *= tot
            else:
                totals[name] += tot
            summary_per_task[infos.index(name)] = yellow(tot)

        table.add_row(summary_per_task)
        current_category = task[:task.rfind('--')-1] if task.count('--')>1 and not 'L3 Res' in task else  task
        if not previous_category:
            previous_category = current_category
            total_epr_previous_category = deepcopy(total_epr_per_task)
        elif previous_category == current_category:
            for x in total_epr_per_task:
                if x=='agreed' or x=='approved':
                    total_epr_previous_category[x] *= total_epr_per_task[x]
                else:
                    total_epr_previous_category[x] += total_epr_per_task[x]
        else:
            summary_per_category = ['' for x in infos]
            summary_per_category[infos.index('task')] = blue('Total '+previous_category)
            tot_per_category = EPR_expected_per_category(previous_category)
            totals['note'] += tot_per_category
            summary_per_category[infos.index('note')] = blue('Exp: '+str(tot_per_category))
            for name, tot in total_epr_previous_category.items():
                summary_per_category[infos.index(name)] = blue(tot)
            table_totals.add_row(summary_per_category)
            previous_category = current_category
            total_epr_previous_category = deepcopy(total_epr_per_task)
        summary_per_task[infos.index('task')] = yellow('Total '+task)
        table_totals.add_row(summary_per_task)
        if args.expand:
            print(table,'\n')

    summary = ['' for x in infos]
    summary[infos.index('task')] = cyan('Total')
    for tot in totals:
        summary[infos.index(tot)] = cyan(totals[tot])
    table_totals.add_row(summary)
    print('\n'*12,table_totals,'\n')



if __name__ == '__main__':
    main()
