"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # make a loop to hit a node with child
        temp = head
        list1 = []
        while temp != None:
            if temp.child != None: #node has child
                #store next value of temp :
                nextNode = temp.next
                if nextNode != None:
                    list1.append(nextNode)
                #making child node add into main list on one side
                child = temp.child
                temp.next = child
                child.prev = temp
                temp.child = None
                # transfering temp to child branch
                temp = child
            elif temp.next == None: #reach EOL
                if len(list1) != 0:
                    print(list1)
                    next = list1.pop()
                    temp.next = next
                    next.prev = temp
                    temp == temp.next
                else:
                    return head
            else:
                temp = temp.next
                    
        return head
                