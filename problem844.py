# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 23:08:36 2022

@author: divya
"""

# 2 strings, # = backspace. compare at end

def backspaceCompare(self, s: str, t: str) -> bool:
    stemp = []
    ttemp = []
    for i in s:
        if i == '#':
            stemp.pop(-1)
        else:
            stemp.append(i)
    for i in t:
        if i == '#':
            ttemp.pop(-1)
        else:
            ttemp.append(i)
    if stemp == ttemp:
        return True
    else:
        return False