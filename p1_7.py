# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 11:53:18 2019

@author: user
"""

class Solution:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
    def HasSubtree(self, pRoot1, pRoot2):
        if not pRoot1:
            return False
        if not pRoot2:
            return False
        if pRoot1.val != pRoot2.val:
            return False
        return self.is_subtree(pRoot1,pRoot2) or self.HasSubtree(pRoot1.left,pRoot2) or self.HasSubtree(pRoot1.right,pRoot2)
    
    def is_subtree(self,A,B):
        if not B:
            return True
        if not A:
            return False
        if A.val != B.val:
            return False
        else:
            return self.is_subtree(A.left,B.left) and self.is_subtree(A.right,B.right)
                
