#!/usr/bin/env python
# -*- cording: utf-8 -*-
__author__ = 'skobayashi'

import sys

class Bcolors(object):
    LOGV = '\033[94m'
    LOGI = '\033[93m'
    LOGD = '\033[92m'
    LOGW = '\033[95m'
    LOGE = '\033[91m'
    ENDC = '\033[0m'

    @classmethod
    def color_print(cls, str, color):
        print color + str + cls.ENDC

def color_logcat():
    try:
        for line in iter(sys.stdin.readline, ""):
            p = line.find('/')
            if 'I' in line[p - 1]:
                Bcolors.color_print(line.strip(), Bcolors.LOGI)
            elif 'V' in line[p - 1]:
                Bcolors.color_print(line.strip(), Bcolors.LOGV)
            elif 'D' in line[p - 1]:
                Bcolors.color_print(line.strip(), Bcolors.LOGD)
            elif 'W' in line[p - 1]:
                Bcolors.color_print(line.strip(), Bcolors.LOGW)
            elif 'E' in line[p - 1]:
                Bcolors.color_print(line.strip(), Bcolors.LOGE)
            else:
                print line.strip()

    except IndexError:
        sys.exit()


def check_including_target(args, line):
    for target in args:
        if target in line:
            return True
    return False


def color_target_line(args):
    try:
        for line in iter(sys.stdin.readline, ""):
            if check_including_target(args, line):
                Bcolors.color_print(line.strip(), Bcolors.LOGE)
            else:
                print line.strip()
    except IndexError:
        sys.exit()


if __name__ == "__main__":
    args = sys.argv
    if len(args) > 0:
        color_target_line(args)
    else:
        color_logcat()
