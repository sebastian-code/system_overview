#! /usr/bin/python3
# -*- coding:utf-8 -*-

from collections import OrderedDict


def meminfo():
    ''' Return the information in /proc/meminfo
    as a dictionary '''
    meminfo = OrderedDict()

    with open('/proc/meminfo') as f:
        for line in f:
            meminfo[line.split(':')[0]] = line.split(':')[1].strip()

    return meminfo

if __name__ == '__main__':
    meminfo = meminfo()
    print('Total memory: {0}'.format(meminfo['MemTotal']))
    print('Free memory: {0}'.format(meminfo['MemFree']))
    print('Total Swap: {0}'.format(meminfo['SwapTotal']))
    print('Free Swap: {0}'.format(meminfo['SwapFree']))
