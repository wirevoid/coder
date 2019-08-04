# -*- coding: utf-8 -*-
"""
Created on Wed May 22 22:25:51 2019

@author: user
"""

from __future__ import print_function
def bubble_sort(collection):
    length = len

if __name__ == '__main__':
    try:
        raw_input
    except NameError:
        raw_input = input
    user_input = raw_input('Enter numbers separated by a comma:').strip()
    unsorted = [int(item) for item in user_input.split(',')]
    print(*bubble_sort(unsorted), sep=',')