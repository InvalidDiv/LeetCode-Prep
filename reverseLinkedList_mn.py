# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 18:36:45 2022

@author: divya
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        p1 = head
        count = 1
        start = p1
        while(count < left):
            start = p1
            p1 = p1.next
            count+=1
        newList = None
        tail = p1
        while (count <= right):
            next = p1.next
            p1.next = newList
            newList = p1
            p1 = next
            count+=1
        
        start.next = newList
        tail.next = p1
        if left > 1:
            return head
        else:
            return newList