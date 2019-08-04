# -*- coding: utf-8 -*-
"""
Created on Tue May 28 21:43:34 2019

@author: user
"""

class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self,node):
        self.stack1.append(node)
    def pop(self):
        if self.stack2 == []:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if self.stack2:
            return self.stack2.pop()
        