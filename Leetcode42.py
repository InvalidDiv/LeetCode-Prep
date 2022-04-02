# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 21:55:35 2022

@author: divya
"""

class Solution:
    def trap(self, height: List[int]) -> int:
        #declare Pointers and maxes
        pL = 0
        pR = len(height)
        maxL = height[pL]
        maxR = height[pR]
        total= 0
        #declare loop
        while pL < pR:
            #left side move up
            if height[pL] <= height[pR]:
                pL+=1
                if min(maxL,maxR) > height[pL]:
                    total+=min(maxL,maxR) - height[pL]
                if height[pL] > maxL:
                    maxL = height[pL]
            else:
                pR-=1
                if min(maxL,maxR) > height[pR]:
                    total+=min(maxL,maxR) - height[pR]
                if height[pR] > maxR:
                    maxR = height[pR]
        return total