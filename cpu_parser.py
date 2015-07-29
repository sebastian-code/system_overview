#! /usr/bin/python3
# -*- coding:utf-8 -*-

from collections import OrderedDict


def cpuinfo_dict():
    ''' Return the information in /proc/cpuinfo
    as a dictionary in the following format:
    cpu_info['proc0']={...}
    cpu_info['proc1']={...}
    '''
    cpuinfo = OrderedDict()
    procinfo = OrderedDict()
    nprocs = 0
    with open('/proc/cpuinfo') as f:
        for line in f:
            if not line.strip():
                # end of one processor
                cpuinfo['proc%s' % nprocs] = procinfo
                nprocs = nprocs+1
                # Reset
                procinfo = OrderedDict()
            else:
                if len(line.split(':')) == 2:
                    procinfo[line.split(':')[0].strip()] = line.split(':')[1].strip()
                else:
                    procinfo[line.split(':')[0].strip()] = ''

    return cpuinfo

if __name__ == '__main__':
    data = cpuinfo_dict()
    for processor in data.keys():
        print('Modelo:', data[processor]['model name'])
        print('Fabricante:', data[processor]['vendor_id'])
        print('Velocidad:', data[processor]['cpu MHz'])
        print('Cache:', data[processor]['cache size'])
        if 'lm' in data[processor]['flags']:
            print('Arquitectura:', '64-bits')
        else:
            print('Arquitectura:', '32-bit')

        break
