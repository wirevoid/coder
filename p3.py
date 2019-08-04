# -*- coding: utf-8 -*-
"""
Created on Sun May 19 11:23:37 2019

@author: user
"""
#create a Node
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def printListFromTailToHead(self,listNode):
        alist = []
        while listNode:
            alist.append(listNode.val)
            listNode = listNode.next
        return alist[::-1]            