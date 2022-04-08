# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 12:41:51 2022

@author: divya
"""

def palin(s: str):
        s = s.lower()
        p1 = 0
        p2 = len(s)-1
        while p1 < p2:
            if s[p1].isalnum() and s[p2].isalnum():
                if s[p1] != s[p2]:
                    return [False,p1,p2]
                else:
                    p1+=1
                    p2-=1
            else:
                if s[p1].isalnum() == False:
                    p1+=1
                if s[p2].isalnum() == False:
                    p2-=1
        return [True,int,int]


class Solution:
    def validPalindrome(self, s: str) -> bool:
        ans = palin(s)
        if ans[0] == False:
            if palin(s[0:ans[1]]+s[ans[1]+1:])[0] == True or palin(s[0:ans[2]]+s[ans[2]+1:])[0] == True:
                return True
            else:
                return False
        else:
            return True